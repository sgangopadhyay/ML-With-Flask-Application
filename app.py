# app.py
# Main Flask file

from flask import Flask
from flask import request
from flask import render_template

# create an object of the class Flask
app = Flask(__name__)

# URL for home-page/index web page
@app.route("/")
def index():
    return "This is the index page for the Flask and ML application"

@app.route("/suman")
def suman():
    return "This is the web-page for Suman Gangopadhyay !"

@app.route("/guvi")
def guvi():
    return "This is the webpage for Guvi !"


# Flask server

if __name__ == "__main__":
    app.run(port=5000, debug=True)
