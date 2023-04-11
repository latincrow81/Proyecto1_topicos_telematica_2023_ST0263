import os
from flask import Flask
from app.services import serve
from .momdb import db, Config
from .models import Queue, Topic


def create_app(environment='development'):

    from .config import config
    from .views import main_blueprint

    # Instantiate app.
    app = Flask(__name__)

    env = os.environ.get('FLASK_ENV', environment)
    app.config.from_object(config[env])
    config[env].configure(app)

    db.init_app(app)

    with app.app_context():
        # crear las tablas si no existen
        db.create_all()
    # start grpc server
    serve()
    return app

