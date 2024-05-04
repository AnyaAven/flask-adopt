""" Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
dbx = db.session.execute

class Pet(db.Model):
    """ Pet class """

    __tablename__ = "pets"

    id = db.mapped_column(
        db.Integer,
        db.Identity(),
        primary_key=True
    )

    name = db.mapped_column(
        db.String(50),
        nullable=False
    )

    species = db.mapped_column(
        db.String(100),
        db.CheckConstraint("species IN" + "('dog', 'cat', 'porcupine')"),
        nullable=False
    )

    photo_url = db.mapped_column(
        db.String(2048),  #NOTE: could be db.Text
        default='',
        nullable=False
    )

    age = db.mapped_column(
        db.String(50),
        db.CheckConstraint("age IN" + "('baby', 'young', 'adult', 'senior')"),
        nullable=False
    )

    notes = db.mapped_column(
        db.Text,
        default='',
        nullable=False
    )

    available = db.mapped_column(
        db.Boolean,
        default=True,
        nullable=False
    )



