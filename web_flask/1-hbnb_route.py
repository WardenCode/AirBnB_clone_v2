#!/usr/bin/python3
"""Initialize a Flask application with two routes"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Display a standard message on get petition"""
    return ('Hello HBNB!')


@app.route("/hbnb", strict_slashes=False)
def main():
    """Display HBNB!"""
    return ('HBNB')


if (__name__ == '__main__'):
    app.run(host="0.0.0.0", port=5000)
