#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """This script starts a Flask web application"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Redirects you to the root path"""
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def c(text):
    """Redirects you to the c/text route"""
    if "_" in text:
        new_text = text.replace("_", " ")
        return "C {}".format(new_text)
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def python(text="is_cool"):
    """Redirects you to the python route and python/text"""
    if "_" in text:
        new_text = text.replace("_", " ")
        return "Python {}".format(new_text)
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Redirects you to the number route and number/n"""
    if type(n) == int:
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Redirects you to the number_template route and number_template/n"""
    if type(n) == int:
        return render_template("5-number.html", data=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
