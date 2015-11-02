"""Forms for public tech_quote website."""

from flask.ext.wtf import Form
from wtforms import TextField, SelectField
from wtforms.validators import DataRequired

from tech_quote.database import Category


class AddQuoteForm(Form):

    """Form for adding new quotes."""

    quotation = TextField('Quotation', validators=[DataRequired()])
    source = TextField('Source', validators=[DataRequired()])
    category = SelectField('Category', validators=[DataRequired()])
    author = SelectField('Author', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Initialize Form and set category choices."""
        Form.__init__(self, *args, **kwargs)

        categories = Category.query.with_entities(
            Category.id, Category.name).order_by(Category.name)
        self.category.choices = categories

        self.author.choices = ((1, 'Sadie'), (2, 'Monty'))
