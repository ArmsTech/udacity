"""Quote views for logged-in tech_quote users (add_quote, etc...)."""

from flask import (
    Blueprint, flash, redirect, request, render_template, url_for)
from flask.ext.login import login_required

from tech_quote.models.quote import Quote
from tech_quote.quote.forms import QuoteForm

blueprint = Blueprint('quote', __name__, static_folder='../static')


@blueprint.route('/add', methods=('GET', 'POST'))
@login_required
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

    return render_template('quote/quote.html', form=form, form_action='Add')


@blueprint.route('/edit/<int:quote_id>', methods=('GET', 'POST'))
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
        'quote/quote.html', form=form, form_action='Update')
