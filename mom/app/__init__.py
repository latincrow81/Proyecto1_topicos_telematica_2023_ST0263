import os
from flask import Flask
from app.services import serve
from app.momdb import db


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
        # Crear las tablas si no existen
        db.create_all()

    # Iniciar el servidor gRPC
    serve()
    return app


app = create_app()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

