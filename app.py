"""Flask app for adopt app."""

import os

from flask import Flask, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, dbx, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.config['SECRET_KEY'] = "secret"
db.init_app(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get("/")
def home():
    """ Display homepage with the list of pets """

    q_pets = db.select(Pet).order_by(Pet.available) # TODO: Does this order correctly?
    pets = dbx(q_pets).scalars().all()

    return render_template(
        "pet_listings.jinja",
        pets=pets
    )
