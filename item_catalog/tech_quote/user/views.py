"""User views for tech_quote."""

from flask import Blueprint

blueprint = Blueprint('user', __name__, static_folder='../static')
