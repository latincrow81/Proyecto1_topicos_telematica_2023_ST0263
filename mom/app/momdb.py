import os
from .models import db


def init_db(app):
    db_path = os.path.join(app.root_path, 'db', 'mom.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    db.init_app(app)
    with app.app_context():
        db.create_all()

