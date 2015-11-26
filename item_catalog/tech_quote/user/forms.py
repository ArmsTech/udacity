"""Forms for handling users."""

from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import InputRequired, Length

from tech_quote.models.user import User


class SettingsForm(Form):

    """Form for updating user settings."""

    user_name = TextField(
        'Name', validators=[InputRequired(), Length(1, 200)])

    def __init__(self, *args, **kwargs):
        """Initialize Form."""
        Form.__init__(self, *args, **kwargs)

    def get_post_invalid_message(self):
        """Get the default error message for a invalid post request."""
        field_to_label = {
            'quote_text': 'Quotation', 'quote_source': 'Source',
            'category_name': 'Category', 'author_name': 'Author',
            'author_bio': 'Biography'}

        error_fields = sorted(self.errors.keys())
        field_or_fields = 'fields' if len(error_fields) > 1 else 'field'

        return "Invalid data provided for {0}: {1}".format(
            field_or_fields,
            ', '.join(map(lambda f: field_to_label[f], error_fields)))
