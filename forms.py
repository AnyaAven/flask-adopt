"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SelectField
from wtforms.validators import URL, InputRequired, Optional


class AddPetForm(FlaskForm):
    """Form for adding new pets"""

    #TODO: validate name length to match database constraint
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
    
    #TODO: make notes optional
    notes = TextAreaField("Pet Notes")

class EditPetForm(FlaskForm):
    """Form for editing pet details"""

    photo_url = StringField(
        "Pet Photo",
        validators=[
            URL(
                require_tld=False,
                message="Invalid Image URL!"),
            Optional()
        ],
    )
    
    #TODO: make notes optional
    notes = TextAreaField("Pet Notes")
    available = BooleanField("Pet available for adoption")