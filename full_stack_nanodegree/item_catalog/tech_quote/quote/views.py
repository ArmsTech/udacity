"""Quote views for logged-in tech_quote users (add a quote, etc...)."""

from flask import (
    Blueprint, abort, flash, jsonify, redirect, request, url_for)
from flask.ext.login import login_required, current_user

from tech_quote.models.quote import Quote, Category
from tech_quote.quote.forms import QuoteForm
from tech_quote.utils import with_template

blueprint = Blueprint(
    'quote', __name__, static_folder='../static',
    template_folder='templates/quote')


@blueprint.route('/api/v1/quotes')
def quotes():
    """Get all quotes and return in JSON format.

    Returns:
        str: All quotes for all users.
    """
    quotes = []

    for quote in Quote.query.all():
        quotes.append({
            'quote': quote.quote_text,
            'source': quote.quote_source,
            'created': quote.quote_created,
            'author': {
                'name': quote.author.author_name,
                'bio': quote.author.author_bio
            },
            'category': {
                'name': quote.category.category_name,
                'description': quote.category.category_description
            }
        })

    return jsonify({'quotes': quotes})


@blueprint.route('/<int:quote_id>')
@with_template()
def quote(quote_id):
    """Show a single quote.

    Args:
        quote_id (int): Id of quote to show.

    Returns:
        dict: Keyword arguments for quote/quote.html
    """
    quote = Quote.query.get_or_404(quote_id)
    return dict(quote=quote)


@blueprint.route('/category/<int:category_id>')
@blueprint.route('/category/<int:category_id>/<int:page>')
@with_template()
def category(category_id, page=1):
    """Show a quote category.

    Args:
        category_id (int): Id of caterogy to show.
        page (int): Page of quotes to render. Defaults to page 1.

    Returns:
        dict: Keyword arguments for quote/category.html
    """
    category = Category.query.get_or_404(category_id)
    quotes = Quote.get_quotes_with_pagination(page, category_id=category_id)

    prev_page = url_for(
        'quote.category', category_id=category_id, page=quotes.prev_num)
    next_page = url_for(
        'quote.category', category_id=category_id, page=quotes.next_num)

    return dict(
        category=category, quotes=quotes,
        prev_page=prev_page, next_page=next_page)


@blueprint.route('/add', methods=('GET', 'POST'))
@login_required
@with_template('quote/add_or_edit.html')
def add():
    """Add a quote.

    Returns:
        dict: Keyword arguments for quote/add_or_edit.html
    """
    form = QuoteForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            Quote.create(
                quote_text=form.quote_text.data,
                quote_source=form.quote_source.data,
                author_id=form.get_selected_author_id(),
                category_id=form.category_name.data,
                user_id=current_user.user_id)

            flash("Quote created", 'success')
            return redirect(url_for('public.index'))
        else:
            flash(form.get_post_invalid_message(), 'danger')

    return dict(form=form, form_action='add')


@blueprint.route('/edit/<int:quote_id>', methods=('GET', 'POST'))
@login_required
@with_template('quote/add_or_edit.html')
def edit(quote_id):
    """Edit a quote.

    Args:
        quote_id (int): Id of quote to edit.

    Returns:
        dict: Keyword arguments for quote/add_or_edit.html
    """
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
            return redirect(url_for('public.index'))
        else:
            flash(form.get_post_invalid_message(), 'danger')

    return dict(quote=quote, form=form, form_action='edit')


@blueprint.route('/delete/<int:quote_id>', methods=('POST',))
@login_required
def delete(quote_id):
    """Delete a quote.

    Args:
        quote_id (int): Id of quote to delete.

    Returns:
        object: Response object to redirect client to where they came from.
    """
    quote = Quote.query.filter_by(quote_id=quote_id).first_or_404()

    if quote.is_owned_by(current_user):
        quote.delete()
        flash("Quote deleted", 'success')
        return redirect(url_for('public.index'))
    else:
        abort(401)
