"""Public views for tech_quote (homepage, etc...)."""

from flask import (
    Blueprint, flash, redirect, request, render_template, url_for)

from tech_quote.public.forms import QuoteForm
from tech_quote.database import Author, Quote

blueprint = Blueprint('public', __name__, static_folder='../static')


@blueprint.route('/')
@blueprint.route('/quotes')
def homepage():
    """Render TQ Homepage."""
    return render_template('layout.html')


@blueprint.route('/quotes/add', methods=('GET', 'POST'))
def add_quote():
    """Add a quote."""
    form = QuoteForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        try:
            # New or existing (id of existing) author?
            int(form.author_name.data)
        except ValueError:
            # We have a new author to create
            author_id = Author.create(
                author_name=form.author_name.data,
                author_bio=form.author_bio.data).author_id
        else:
            author_id = form.author_name.data

        Quote.create(
            quote_text=form.quote_text.data,
            quote_source=form.quote_source.data,
            author_id=author_id, category_id=form.category_name.data)

        flash("Quote created", 'success')
        return redirect(url_for('public.homepage'))
    else:
        errors = sorted(form.errors.keys())
        field_or_fields = 'fields' if len(errors) > 1 else 'field'
        flash("Invalid data provided for {0}: {1}".format(
            field_or_fields, ', '.join(errors)), 'danger')

    return render_template('public/quote.html', form=form, form_action='Add')


@blueprint.route('/quotes/edit/<int:quote_id>', methods=('GET', 'POST'))
def edit_quote(quote_id):
    """Edit a quote."""
    quote = Quote.query.filter_by(quote_id=quote_id).first_or_404()

    form = QuoteForm(
        request.form, obj=quote,
        category_name=quote.category.category_id,
        author_name=quote.author.author_id,
        author_bio=quote.author.author_bio)

    return render_template('public/quote.html', form=form, form_action='Edit')
