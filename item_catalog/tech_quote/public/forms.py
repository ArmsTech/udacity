"""Forms for public tech_quote website."""

import operator

from flask.ext.wtf import Form
from wtforms import TextField, SelectField
from wtforms.validators import InputRequired, Length, ValidationError

from tech_quote.database import Category

EMPTY_OPTION = ("", "")


class DynamicSelectField(SelectField):

    """SelectField that allows user-added select field options."""

    def pre_validate(self, form):
        """Skip pre-validation (ensuring choice is in choices)."""
        pass


class AddQuoteForm(Form):

    """Form for adding new quotes."""

    quotation = TextField('Quotation', validators=[InputRequired()])
    source = TextField('Source', validators=[InputRequired(), Length(1, 200)])
    category = SelectField('Category', validators=[InputRequired()])
    author = DynamicSelectField(
        'Author', validators=[InputRequired(), Length(1, 70)])
    biography = TextField(
        'Biography', validators=[InputRequired(), Length(1, 200)])

    def __init__(self, *args, **kwargs):
        """Initialize Form and set category choices."""
        Form.__init__(self, *args, **kwargs)

        categories = Category.query.with_entities(
            Category.id, Category.name).order_by(Category.name).all()
        self.category.choices = [EMPTY_OPTION] + map(
            lambda (id_, value): (str(id_), value), categories)

        self.author.choices = (EMPTY_OPTION, (1, 'Sadie'), (2, 'Monty'))

    def validate_author(self, field):
        """Validate author hybrid select/text field."""
        author = field.data
        if type(author) == int:
            # An existing author (id) was selected let's make sure it's valid
            author_ids = map(operator.itemgetter(0), self.author.choices)
            if author not in author_ids:
                raise ValidationError("Author must not be a number")
