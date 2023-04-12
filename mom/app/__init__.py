import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.services import serve

db = SQLAlchemy()


def create_app(environment='development'):

    from .config import config
    from .views import main_blueprint

    # Instantiate app.
    app = Flask(__name__)

    env = os.environ.get('FLASK_ENV', environment)
    app.config.from_object(config[env])
    config[env].configure(app)

    # iniciar db
    db.init_app(app)


    # start grpc server
    serve()

    return app
