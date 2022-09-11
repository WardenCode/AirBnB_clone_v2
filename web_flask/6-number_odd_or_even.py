#!/usr/bin/python3
"""
Initialize a Flask application with six routes,
using variables and rendering templates
"""
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Display a standard message on get petition"""
    return ('Hello HBNB!')


@app.route("/hbnb", strict_slashes=False)
def main():
    """Display HBNB!"""
    return ('HBNB')


@app.route("/c/<string:text>", strict_slashes=False)
def c_is_fun(text):
    """Display C followed by text"""
    return ('C {:s}'.format(escape(text)).replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def python_is_cool(text='is cool'):
    """
    Display Python followed by text.
    text by default is 'is cool'
    """
    return ('Python {:s}'.format(escape(text)).replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def is_a_number(n):
    """Display the int passed by the URL"""
    return ('{:d} is a number'.format(escape(n)))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display the int on a h1 tag"""
    return (render_template('5-number.html', num=escape(n)))


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Display the int on a h1 tag"""
    return (render_template('6-number_odd_or_even.html', num=n))


if (__name__ == '__main__'):
    app.run(host="0.0.0.0", port=5000)
