"""User views for tech_quote."""

from flask import Blueprint, render_template

from tech_quote.models.user import User

blueprint = Blueprint('user', __name__, static_folder='../static')


@blueprint.route('/<user_login>')
def profile(user_login):
    """Render a user's profile."""
    user = User.query.filter_by(user_github_login=user_login).first_or_404()
    return render_template('user/profile.html', user=user)
