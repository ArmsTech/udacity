"""Public views for tech_quote (homepage, etc...)."""

from flask import Blueprint, redirect, request, render_template, url_for

from tech_quote.public.forms import AddQuoteForm

blueprint = Blueprint('public', __name__, static_folder='../static')


@blueprint.route('/')
@blueprint.route('/quotes')
def homepage():
    """Render TQ Homepage."""
    return render_template('layout.html')


@blueprint.route('/quotes/add', methods=('GET', 'POST'))
def add_quote():
    """Add a quotation."""
    form = AddQuoteForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            return redirect(url_for("public.layout"))
        else:
            print "FLASH/LOG AN ERROR HERE!"

    return render_template('public/add.html', form=form)
