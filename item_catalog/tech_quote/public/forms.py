"""Forms for public tech_quote website."""

from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired


class AddQuoteForm(Form):

    """Form for adding new quotes."""

    quotation = TextField('Quotation', validators=[DataRequired()])
    source = TextField('Source', validators=[DataRequired()])
