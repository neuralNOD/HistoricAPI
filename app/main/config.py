# -*- encoding: utf-8 -*-

import os

basedir    = os.path.abspath(os.path.dirname(__file__)) # base directory
local_base = os.getenv("DATABASE_URL", "sqlite:///")

class Config:
    """Base Configuration Class - Inherited by Others"""

    DEBUG      = False
    TESTING    = False
    SECRET_KEY = os.getenv("SECRET_KEY", "my_secret_key")


class DevelopmentConfig(Config):
    """Development Configuration: invoke this using config_name = dev"""

    DEBUG = True # This is a development server.

    # set database
    SQLALCHEMY_DATABASE_URI = f"{local_base}/{os.getenv('dev_db', 'dev-database.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """Testing Environment: invoke this using config_name = test"""

    DEBUG   = True
    TESTING = True

    # set database
    SQLALCHEMY_DATABASE_URI = f"{local_base}/{os.getenv('test_db', 'test-database.db')}"

    PRESERVE_CONTEXT_ON_EXCEPTION  = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Production Environment: invoke this using config_name = prod"""

    pass # configure for production environment here

config_by_name = dict(
        dev  = DevelopmentConfig,
        test = TestingConfig,
        prod = ProductionConfig
    )

key = Config.SECRET_KEY
