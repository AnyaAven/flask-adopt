"""Flask app for adopt app."""

import os

from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import desc

from models import db, dbx, Pet
from forms import AddPetForm, EditPetForm

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
def show_pet_listings():
    """ Display homepage with the list of pets, sorted by availability"""

    q_pets = db.select(Pet).order_by(desc(Pet.available))
    pets = dbx(q_pets).scalars().all()

    return render_template(
        "pet/pet_listings.jinja",
        pets=pets
    )

@app.route("/add", methods=["GET", "POST"])
def show_add_pet_form():
    """Show add pet form"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes
        )

        db.session.add(pet)
        db.session.commit()

        flash(f"Added {pet.name} successfully!")

        return redirect("/")

    else:
        return render_template("pet/pet_form.jinja", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def display_or_edit_pet(pet_id):
    """ Display the pet's profile OR edit the profile"""

    pet = db.get_or_404(Pet, pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        flash(f"{pet.name} profile edited successfully!")

        return redirect(f"/{pet_id}")

    else:
        return render_template("pet/pet_profile.jinja", form=form, pet=pet)