#!/usr/bin/python3
"""Initialize a Flask application with three routes"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Display a standard message on get petition"""
    return ('Hello HBNB!')


@app.route("/hbnb", strict_slashes=False)
def main():
    """Display HBNB!"""
    return ('HBNB!')


@app.route("/c/<string:text>", strict_slashes=False)
def c_is_fun(text):
    """Display C followed by text"""
    return ('C {:s}'.format(escape(text)).replace('_', ' '))


if (__name__ == '__main__'):
    app.run(host="0.0.0.0", port=5000)
