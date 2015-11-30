"""Flask application for tech_quote."""

import os

from flask import Flask, render_template
from flask.ext.uploads import configure_uploads, patch_request_class

from tech_quote import public, quote, user
from tech_quote.extensions import avatars, db, login_manager, migrate
from tech_quote.assets import assets


def create_app():
    """Create a tech_quote application.

    Returns:
        Flask: The tech_quote application.
    """
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    register_extensions(app)
    register_blueprints(app)
    register_errors(app)
    # Register app with Flask-Uploads and limit upload size to 16MB
    configure_uploads(app, (avatars,))
    patch_request_class(app)

    return app


def register_extensions(app):
    """Register flask extensions.

    Args:
        app (object): Flask application object.
    """
    db.init_app(app)
    assets.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    """Register flask blueprints.

    Args:
        app (object): Flask application object.
    """
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(user.views.blueprint, url_prefix='/user')
    app.register_blueprint(quote.views.blueprint, url_prefix='/quote')


def register_errors(app):
    """Register flask error handlers.

    Args:
        app (object): Flask application object.
    """
    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return render_template(
            'errors/{0}.html'.format(error_code)), error_code

    for error in (401, 404, 500):
        app.errorhandler(error)(render_error)
