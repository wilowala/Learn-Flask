from flask import Flask 

app = Flask(__name__)

@app.route("/")
def intro():

    return "Hello, Here's my first flask app!"