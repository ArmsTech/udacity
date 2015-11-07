"""Forms for public tech_quote website."""

import operator

from flask.ext.wtf import Form
from wtforms import TextField, SelectField
from wtforms.validators import InputRequired, Length, URL, ValidationError

from tech_quote.database import Author, Category

EMPTY_OPTION = ("", "")


class DynamicSelectField(SelectField):

    """SelectField that allows user-added select field options."""

    def pre_validate(self, form):
        """Skip pre-validation (ensuring choice is in choices)."""
        pass


class QuoteForm(Form):

    """Form for adding new quotes."""

    quote_text = TextField('Quotation', validators=[InputRequired()])
    quote_source = TextField(
        'Source', validators=[InputRequired(), Length(1, 200), URL()])
    category_name = SelectField('Category', validators=[InputRequired()])
    author_name = DynamicSelectField(
        'Author', validators=[InputRequired(), Length(1, 70)])
    author_bio = TextField(
        'Biography', validators=[InputRequired(), Length(1, 200), URL()])

    def __init__(self, *args, **kwargs):
        """Initialize Form and set category choices."""
        Form.__init__(self, *args, **kwargs)

        categories = Category.query.with_entities(
            Category.category_id, Category.category_name).order_by(
            Category.category_name).all()
        self.category_name.choices = (
            [EMPTY_OPTION] + self.stringify_choices(categories))

        authors = Author.query.with_entities(
            Author.author_id, Author.author_name).order_by(
            Author.author_name).all()
        self.author_name.choices = (
            [EMPTY_OPTION] + self.stringify_choices(authors))

    def validate_author(self, field):
        """Validate author hybrid select/text field."""
        author = field.data
        try:
            # Is it an id?
            int(author)
        except ValueError:
            # Nope, must be a name. Let it pass.
            return
        else:
            # An existing author (id) was selected let's make sure it's valid
            author_ids = map(operator.itemgetter(0), self.author_name.choices)
            if author not in author_ids:
                raise ValidationError("Author must not be a number")

    def stringify_choices(self, choices):
        """Convert int ids to str representations."""
        return map(lambda (id_, value): (str(id_), value), choices)
