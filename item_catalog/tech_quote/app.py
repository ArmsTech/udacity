"""Flask application for tech_quote."""

from flask import Flask

from tech_quote.settings import ProductionConfig
from tech_quote.extensions import db, migrate


@app.route('/')
def hello_world():
    return 'Hello World!'


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
    return app


def register_extensions(app):
    """Register flask extensions."""
    db.init_app(app)
    migrate.init_app(app, db)


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
