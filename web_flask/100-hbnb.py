#!/usr/bin/python3
"""
Advanced task HBNB is alive
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display the main page of Airbnb"""

    amenities = list(storage.all(Amenity).values())
    states = list(storage.all(State).values())
    places = list(storage.all(Place).values())
    users = storage.all(User)

    return (render_template('/100-hbnb.html', amenities=amenities,
                            states=states, places=places, users=users))


@app.teardown_appcontext
def close_session(self):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if (__name__ == '__main__'):
    app.run(host="0.0.0.0", port=5000)
