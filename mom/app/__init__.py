import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.init_db import init_db
from app.services import serve


def create_app(environment='development'):

    from .config import config
    from .views import main_blueprint

    # Instantiate app.
    app = Flask(__name__)

    env = os.environ.get('FLASK_ENV', environment)
    app.config.from_object(config[env])
    config[env].configure(app)

    init_db()
    # start grpc server
    serve()

    return app
