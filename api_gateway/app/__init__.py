import connexion


def create_app(environment='development'):

    from .config import config

    # Instantiate app.

    app = connexion.FlaskApp(__name__)
    app.add_api('../openapi.yml')
    return app
