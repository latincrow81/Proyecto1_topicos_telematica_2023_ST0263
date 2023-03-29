import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# instantiate extensions
login_manager = LoginManager()
db = SQLAlchemy()


def create_app(environment='development'):

    from .config import config
    from .views import main_blueprint
    from .auth.views import auth_blueprint
    from .auth.models import User, AnonymousUser

    # Instantiate app.


    app = connexion.FlaskApp(__name__)
    app.add_api('../openapi.yml')
    return app
