"""User views for tech_quote."""

from flask import Blueprint, flash, redirect, request, url_for
from flask.ext.login import login_required

from tech_quote.extensions import avatars
from tech_quote.models.user import User
from tech_quote.models.quote import Quote
from tech_quote.user.forms import SettingsForm
from tech_quote.utils import with_template

blueprint = Blueprint(
    'user', __name__, static_folder='../static',
    template_folder='templates/user')


@blueprint.route('/<user_login>')
@blueprint.route('/<user_login>/<int:page>')
@with_template()
def profile(user_login, page=1):
    """Render a user's profile.

    Args:
        user_login (str): `User` login of user to render profile for.
        page (int): Page of user's quotes to render. Defaults to page 1.

    Returns:
        dict: Keyword arguments for user/profile.html
    """
    user = User.query.filter_by(user_github_login=user_login).first_or_404()
    quotes = Quote.get_quotes_with_pagination(
        page, user_id=user.user_id)

    prev_page = url_for(
        'user.profile', user_login=user_login, page=quotes.prev_num)
    next_page = url_for(
        'user.profile', user_login=user_login, page=quotes.next_num)

    return dict(
        user=user, quotes=quotes, prev_page=prev_page, next_page=next_page)


@blueprint.route('/<user_login>/settings', methods=('GET', 'POST'))
@login_required
@with_template()
def settings(user_login):
    """Render a user's profile settings.

    Args:
        user_login (str): `User` login of user to render settings for.

    Returns:
        dict: Keyword arguments for user/settings.html
    """
    user = User.query.filter_by(user_github_login=user_login).first_or_404()
    form = SettingsForm(obj=user)

    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(user)

            file_to_upload = request.files.get(form.user_avatar.name)
            if file_to_upload and file_to_upload.filename:
                file_name = avatars.save(file_to_upload)
                user.user_avatar_url = avatars.url(file_name)

            user.save()

            flash("Settings updated", 'success')
            return redirect(
                url_for('user.profile', user_login=user.user_github_login))
        else:
            flash(form.get_post_invalid_message(), 'danger')

    return dict(form=form, user=user)
