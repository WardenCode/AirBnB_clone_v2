#!/usr/bin/python3
"""
Initialize a Flask application with state_list
(all states or one state depending of URL), using the Storage
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Display the main page of Airbnb"""

    amenities = list(storage.all(Amenity).values())
    states = list(storage.all(State).values())

    return (render_template('/10-hbnb_filters.html', amenities=amenities,
                            states=states))


@app.teardown_appcontext
def close_session(self):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if (__name__ == '__main__'):
    app.run(host="0.0.0.0", port=5000)
