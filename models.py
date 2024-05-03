"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
dbx = db.session.execute

class Pet(db.model):
    """ Pet class """

    __table__ = "pets"

    id = db.mapped_column(
        db.Integer,
        db.Indentity(),
        primary_key=True
    )

    name = db.mapped_column(
        db.String(50),
        nullable=False
    )

    species = db.mapped_column(
        db.String(100),
        nullable=False
    )

    photo_url = db.mapped_column(
        db.String(2048),
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

    available = db.mapped_colum(
        db.Boolean,
        default=True,
        nullable=False
    )



