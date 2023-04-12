# Define your models here.
# You can also define them inside a package and import them here.
# This is only a convenience so that all your models are available from a single module.
from sqlalchemy import Column, Integer, String

from app.init_db import Base


class Queue(Base):
    __tablename__ = 'queue'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)


class Topic(Base):
    __tablename__ = 'topic'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)