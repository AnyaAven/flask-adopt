"""Seed pets to db with data."""

from app import app
from models import db, Pet

app.app_context().push()

db.drop_all()
db.create_all()

mitzy = Pet(
    name="Mitzy",
    species="cat",
    photo_url="https://www.catster.com/wp-content/uploads/2023/12/Gray-striped-cat-_OlhaTsiplyar_shutterstock.jpg.webp",
    age="adult",
    notes="She scratches my carpet with love and she meows a lot"
)
raven = Pet(
    name="Raven",
    species="cat",
    photo_url="https://images.pexels.com/photos/1287365/pexels-photo-1287365.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    age="adult",
    notes="Raven looks at you like you're his entire world. He loves deeply and likes to drool"
)
zoey = Pet(
    name="Zoey",
    species="dog",
    photo_url="https://images.pexels.com/photos/5966250/pexels-photo-5966250.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    age="adult",
    notes="Zoey is a tough Yorkie"
)

gummy = Pet(
    name="Gummy",
    species="cat",
    photo_url="",
    age="senior",
    notes="Very fluffy"
)

porky = Pet(
    name="Porky",
    species="porcupine",
    photo_url="https://cincinnatizoo.org/wp-content/uploads/2023/12/53313821708_d6a5daf4ba_b.jpg",
    age="baby",
    notes="Very fluffy"
)


wombat = Pet(
    name="Wombat",
    species="cat",
    photo_url="https://images.pexels.com/photos/7201820/pexels-photo-7201820.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    age="adult",
    notes="""Meet Midnight, the epitome of elegance and charm wrapped in sleek
    black fur. This fluffy feline's mesmerizing amber eyes are like portals
    to a world of mystery and affection. Midnight's luxuriously soft coat
    invites endless cuddles and strokes, promising warmth and comfort in
    every embrace. With a playful spirit and a gentle demeanor, this
    enchanting companion will captivate your heart with every purr and
    gentle nuzzle. Adopt Midnight today and experience the joy of sharing
    your life with a purr-fectly delightful friend."""
)


db.session.add_all([mitzy, raven, zoey, wombat, porky, gummy]) # FIXME: why are we getting 2 gummys'?
db.session.commit()