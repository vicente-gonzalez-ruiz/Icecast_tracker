import os
from flask import Flask,redirect

app = Flask(__name__)

@app.route('/<x>')
def hello(x):
    return redirect("http://www.example.com", code=302)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
