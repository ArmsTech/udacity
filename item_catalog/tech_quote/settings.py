"""Settings (configuration) for tech_quote application."""

import os


class Config(object):

    """Base configuration."""

    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))


class ProductionConfig(Config):

    """Production configuration."""

    ENV = 'Production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2:///tq'
