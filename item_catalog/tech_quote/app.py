"""Flask application for tech_quote."""

import os

from flask import Flask

from tech_quote import public
from tech_quote.extensions import assets, db, migrate


def create_app():
    """Create a tech_quote application.

    Returns:
        Flask: The tech_quote application.
    """
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    """Register flask extensions."""
    db.init_app(app)
    assets.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    """Register flask blueprints."""
    app.register_blueprint(public.views.blueprint)
