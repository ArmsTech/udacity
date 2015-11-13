"""Public views for tech_quote (homepage, etc...)."""

from flask import (
    Blueprint, flash, redirect, request, render_template, url_for)
from flask.ext.login import login_user, logout_user, login_required

from tech_quote.extensions import login_manager
from tech_quote.models.tq import Quote
from tech_quote.models.user import User
from tech_quote.oauth.providers import GitHubSignIn
from tech_quote.public.forms import QuoteForm

blueprint = Blueprint('public', __name__, static_folder='../static')


@login_manager.user_loader
def load_user(user_id):
    """Reload the user object from the user ID stored in the session."""
    return User.query.get(user_id)


@blueprint.route("/logout")
@login_required
def logout():
    """User will be logged out, and their session will be cleaned up."""
    logout_user()
    return redirect(url_for('public.homepage'))


@blueprint.record_once
def record_params(state):
    """Store app.config in blueprint when blueprint is registered on app."""
    app = state.app
    blueprint.config = {key: value for key, value in app.config.iteritems()}


@blueprint.route('/')
@blueprint.route('/quotes')
@blueprint.route('/quotes/<int:page>', methods=('GET',))
def homepage(page=1):
    """Render TQ Homepage."""
    posts_per_page = blueprint.config['POSTS_PER_PAGE']
    quotes = Quote.query.order_by(
        Quote.quote_created.desc()).paginate(page, posts_per_page)
    return render_template('public/index.html', quotes=quotes)


@blueprint.route('/login/oauth/github')
def login_with_github():
    """Log a user in with GitHub OAuth credentials."""
    return redirect(GitHubSignIn().service.get_authorize_url())


@blueprint.route('/login/oauth/github/authorized')
def handle_github_redirect():
    """Handle redirect from GitHub access request (/login/oauth/github')."""
    code = request.args['code']

    session = GitHubSignIn().service.get_auth_session(data={'code': code})
    github_user_data = session.get('user').json()

    user = User.by_github_id(github_user_data['id'])
    if user is None:
        user = User.create(
            user_email=github_user_data['email'],
            user_name=github_user_data['name'],
            user_github_id=github_user_data['id'],
            user_github_login=github_user_data['login'])

    login_user(user)
    flash("Logged in successfully!", 'success')

    return redirect(url_for('public.homepage'))


@blueprint.route('/quotes/add', methods=('GET', 'POST'))
def add_quote():
    """Add a quote."""
    form = QuoteForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            Quote.create(
                quote_text=form.quote_text.data,
                quote_source=form.quote_source.data,
                author_id=form.get_selected_author_id(),
                category_id=form.category_name.data)

            flash("Quote created", 'success')
            return redirect(url_for('public.homepage'))
        else:
            flash(form.get_post_invalid_message(), 'danger')

    return render_template('public/quote.html', form=form, form_action='Add')


@blueprint.route('/quotes/edit/<int:quote_id>', methods=('GET', 'POST'))
def edit_quote(quote_id):
    """Edit and update a quote."""
    quote = Quote.query.filter_by(quote_id=quote_id).first_or_404()

    form = QuoteForm(
        request.form, obj=quote,
        category_name=quote.category.category_id,
        author_name=quote.author.author_id,
        author_bio=quote.author.author_bio)

    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(quote)
            # Manually update relationship objects in model
            quote.author_id = form.get_selected_author_id()
            quote.author.author_bio = form.author_bio.data
            quote.category_id = form.category_name.data

            # Save updated model to db
            quote.save()

            flash("Quote updated", 'success')
            return redirect(url_for('public.homepage'))
        else:
            flash(form.get_post_invalid_message(), 'danger')

    return render_template(
        'public/quote.html', form=form, form_action='Update')
