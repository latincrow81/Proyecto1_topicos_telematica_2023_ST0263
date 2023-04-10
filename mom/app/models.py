from momdb import db


class Queue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    messages = db.relationship('Message', backref='queue', lazy=True)


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    subscribers = db.relationship('Subscriber', backref='topic', lazy=True)
