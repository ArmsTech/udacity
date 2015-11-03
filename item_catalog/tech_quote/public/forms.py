"""Forms for public tech_quote website."""

from flask.ext.wtf import Form
from wtforms import TextField, SelectField
from wtforms.validators import DataRequired

from tech_quote.database import Category

EMPTY_OPTION = ("", "")


class AddQuoteForm(Form):

    """Form for adding new quotes."""

    quotation = TextField('Quotation', validators=[DataRequired()])
    source = TextField('Source', validators=[DataRequired()])
    category = SelectField('Category', validators=[DataRequired()])
    author = SelectField('Author', validators=[DataRequired()])
    biography = TextField('Biography', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Initialize Form and set category choices."""
        Form.__init__(self, *args, **kwargs)

        categories = Category.query.with_entities(
            Category.id, Category.name).order_by(Category.name).all()
        self.category.choices = [EMPTY_OPTION] + categories

        self.author.choices = (EMPTY_OPTION, (1, 'Sadie'), (2, 'Monty'))
