"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SelectField
from wtforms.validators import URL, InputRequired, Optional


class AddPetForm(FlaskForm):
    """Form for adding new pets"""

    name = StringField("Pet Name", validators=[InputRequired()])

    species = SelectField(
        "Pet Species",
        choices=[('cat', 'Cat'),
                 ('dog', 'Dog'),
                 ('porcupine', 'Porcupine')],
        validators=[InputRequired()]
    )

    photo_url = StringField(
        "Pet Photo",
        validators=[
            URL(
                require_tld=False,
                message="Invalid Image URL!"),
            Optional()
        ],
    )

    age = SelectField(
        "Pet Age",
        choices=[('baby', 'Baby'),
                 ('young', 'Young'),
                 ('adult', 'Adult'),
                 ('senior', 'Senior')],
        validators=[InputRequired()]
    )

    notes = TextAreaField("Pet Notes")
