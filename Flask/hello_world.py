from flask import Flask
app = Flask(__name__)

@app.route("/<x>")
def hello(x):
    return "Hello World!"

if __name__ == "__main__":
    #app.debug = True
    #app.run()
    app.run(host='0.0.0.0', port=5001)
