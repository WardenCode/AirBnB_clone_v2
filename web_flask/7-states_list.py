#!/usr/bin/python3
"""Initialize a Flask application with state_list, using the Storage"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/state_list", strict_slashes=False)
def state_list():
    """Display the list of states"""
    values = storage.all(State).values()
    return (render_template('7-states_list.html', states=values))


@app.teardown_appcontext()
def close_session(self):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if (__name__ == '__main__'):
    app.run(host="0.0.0.0", port=5000)
