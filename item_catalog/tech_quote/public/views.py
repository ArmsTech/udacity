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
    """Add a quotation."""
    form = QuoteForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():

            try:
                # New or existing author?
                int(form.author.data)
            except ValueError:
                # We have a new author to create
                author_id = Author.create(
                    name=form.author.data, biography=form.biography.data).id
            else:
                author_id = form.author.data

            Quote.create(
                text=form.quotation.data, source=form.source.data,
                author_id=author_id, category_id=form.category.data)

            flash("Quote created", 'success')
            return redirect(url_for('public.homepage'))
        else:
            errors = sorted(form.errors.keys())
            field_or_fields = 'fields' if len(errors) > 1 else 'field'
            flash("Invalid data provided for {0}: {1}".format(
                field_or_fields, ', '.join(errors)), 'danger')

    return render_template('public/quote.html', form=form, form_action='Add')
