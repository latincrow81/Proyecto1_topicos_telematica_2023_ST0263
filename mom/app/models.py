from app.momdb import db

class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    queue_id = db.Column(db.Integer, db.ForeignKey('queue.id'))

class Queue(db.Model):
    __tablename__ = 'queue'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    messages = db.relationship('Message', backref='queue', lazy=True)
