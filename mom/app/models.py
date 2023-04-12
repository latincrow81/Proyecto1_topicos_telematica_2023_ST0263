# Define your models here.
# You can also define them inside a package and import them here.
# This is only a convenience so that all your models are available from a single module.
from . import db


class Queue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)