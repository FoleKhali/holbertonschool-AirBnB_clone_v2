#!/usr/bin/python3
"""
this module starts a Flask Web application
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    """ route / will return 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb_hbnb():
    """/hbnb route returns HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def c_hbnb(text):
    """ dynamically grabs route"""
    if text:
        return "C {}".format(text.replace("_", " "))


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>")
def python_hbnb(text):
    """ route /python/ with text afterwards """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def number_hbnb(n):
    """ route only numbers """
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template_hbnb(n):
    """ path to use flask application take in arguement from path"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
