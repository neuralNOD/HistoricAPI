# -*- encoding: utf-8 -*-

"""Main Package for Controlling the API"""

from flask import Flask
from flask_bcrypt import Bcrypt # Bcrypt hashing for Flask
from flask_sqlalchemy import SQLAlchemy

from app.main.config import config_by_name
from app.main._base_model_class import ModelClass

db = SQLAlchemy(model_class = ModelClass)
flask_bcrypt = Bcrypt() # bcrypt hashing utilities


def create_app(config_name : str):
    """Creates Flask Application

    :type  config_name: str
    :param config_name: Configuration for Setting up the Environment, can be
                        any of the following: ['dev', 'test', 'prod']
    """

    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app
