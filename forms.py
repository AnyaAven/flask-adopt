"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import URL

class AddPetForm(FlaskForm):
    name = StringField("Pet Name")
    species = StringField("Pet Species")
    photo_url = StringField("Pet Photo", validators=[URL(require_tld=False, message="Invalid Image URL!")])
    age = StringField("Pet Age")
    notes = TextAreaField("Pet Notes")