"""Settings (configuration) for tech_quote application."""

import os


class Config(object):

    """Base configuration."""

    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    SITE_NAME = 'Tech Quote'
    SECRET_KEY = os.environ['TQ_SECRET']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']


class DevelopmentConfig(Config):

    """Development configuration."""

    ENV = 'Development'

    ASSETS_DEBUG = True
    DEBUG = True
    QUOTES_PER_PAGE = 3
    UPLOADS_DEFAULT_DEST = os.path.join(Config.APP_DIR, 'uploads')


class ProductionConfig(Config):

    """Production configuration."""

    ENV = 'Production'

    DEBUG = False
    QUOTES_PER_PAGE = 10
    # In a production environment we'd store uploads outside the app dir
    UPLOADS_DEFAULT_DEST = os.path.join(Config.APP_DIR, 'uploads')
