"""User views for tech_quote."""

from flask import Blueprint, render_template

blueprint = Blueprint('user', __name__, static_folder='../static')


@blueprint.route('/<int:user_id>')
def profile(user_id):
    """Render a user's profile."""
    return render_template('user/profile.html')
