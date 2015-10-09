"""Public views for tech_quote (homepage, etc...)."""

from flask import Blueprint

blueprint = Blueprint('public', __name__)  # , static_folder="../static")


@blueprint.route('/')
def hello_world():
    return 'Hello World!'
