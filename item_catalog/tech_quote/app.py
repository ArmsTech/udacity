"""Flask application for tech_quote."""

from flask import Flask

from tech_quote import public
from tech_quote.extensions import db, migrate
from tech_quote.settings import ProductionConfig


def create_app(config_object=ProductionConfig):
    """Create a tech_quote application.

    Args:
        config_object (Config): The configuration object to use.

    Returns:
        Flask: The tech_quote application.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    """Register flask extensions."""
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    """Register flask blueprints."""
    app.register_blueprint(public.views.blueprint)


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
