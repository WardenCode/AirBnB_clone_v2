#!/usr/bin/python3
"""Initialize a Flask application with state_list, using the Storage"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Display cities by states"""
    values = storage.all(State).values()
    return (render_template('/8-cities_by_states.html', states=values))


@app.teardown_appcontext()
def close_session(self):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if (__name__ == '__main__'):
    app.run(host="0.0.0.0", port=5000)
