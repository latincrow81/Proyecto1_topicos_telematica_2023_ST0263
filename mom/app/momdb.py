import os
from flask_sqlalchemy import SQLAlchemy

# obtener la ruta absoluta del directorio actual
basedir = os.path.abspath(os.path.dirname(__file__))


# configuración de la base de datos SQLite
class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "mom.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# instancia de la base de datos
db = SQLAlchemy()


def get_session():
    return db.session
