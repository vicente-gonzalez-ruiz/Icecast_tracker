import os
from flask import Flask, redirect
import socket
import threading
import queue

def time_connection(server, queue):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(server)
        print ("Connected to " + str(server))
        if queue.empty:
            queue.put(server)
        s.close()
    except:
        print(str(server) + " does not respond!")

app = Flask(__name__)

@app.route('/<mountpoint>')
def get_mountpoit(mountpoint):
    q = queue.Queue()
    data = open("servers.txt")
    for line in data:
        (host, port) = line.split(':')
        port = int(port)
        server = (host, port)
        print("Processing server: " + str(server))
        threading.Thread(target=time_connection, args=(server, q)).start()

    tmp = q.get()
    selected_server = tmp[0] + ':' + str(tmp[1])
    url = 'http://' + selected_server + '/' + str(mountpoint)
    print("Selected server: " + url)
    
    return redirect(url, code=302)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5001.
    port = int(os.environ.get('PORT', 5001))
    #app.debug = True # Uncomment me for Web debugging
    app.run(host='0.0.0.0', port=port)
