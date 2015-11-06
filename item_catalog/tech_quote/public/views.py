"""Public views for tech_quote (homepage, etc...)."""

from flask import Blueprint, redirect, request, render_template, url_for

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

            # If we receive String data we have a new author to create
            if type(form.author.data) in (unicode, str):
                author_id = Author.create(
                    name=form.author.data, biography=form.biography.data).id
            else:
                author_id = form.author.data

            Quote.create(
                text=form.quotation.data, source=form.source.data,
                author_id=author_id, category_id=form.category.data)

            return redirect(url_for('public.homepage'))
        else:
            print form.errors
            print "FLASH/LOG AN ERROR HERE!"

    return render_template('public/quote.html', form=form, form_action='Add')
