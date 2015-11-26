"""User views for tech_quote."""

from flask import Blueprint, render_template, request, url_for
from flask.ext.login import login_required

from tech_quote.models.user import User
from tech_quote.models.quote import Quote
from tech_quote.user.forms import SettingsForm

blueprint = Blueprint('user', __name__, static_folder='../static')


@blueprint.route('/<user_login>')
@blueprint.route('/<user_login>/<int:page>')
def profile(user_login, page=1):
    """Render a user's profile."""
    user = User.query.filter_by(user_github_login=user_login).first_or_404()
    quotes = Quote.get_quotes_with_pagination(
        page, user_id=user.user_id)

    prev_page = url_for(
        'user.profile', user_login=user_login, page=quotes.prev_num)
    next_page = url_for(
        'user.profile', user_login=user_login, page=quotes.next_num)

    return render_template(
        'user/profile.html', user=user, quotes=quotes,
        prev_page=prev_page, next_page=next_page)


@blueprint.route('/<user_login>/settings')
@login_required
def settings(user_login):
    """Render a user's profile."""
    user = User.query.filter_by(user_github_login=user_login).first_or_404()

    form = SettingsForm(request.form, obj=user)

    return render_template('user/settings.html', form=form, user=user)
