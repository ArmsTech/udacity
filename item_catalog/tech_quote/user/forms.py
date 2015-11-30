"""Forms for handling users."""

import re

from flask.ext.wtf import Form
from wtforms import FileField, TextField
from wtforms.validators import InputRequired, Length, ValidationError

AVATAR_RE = re.compile(r'^[^\\/]+\.(?:jpg|jpe|jpeg|png|gif|svg|bmp)$')


class SettingsForm(Form):

    """Form for updating user settings."""

    user_name = TextField(
        'Name', validators=[InputRequired(), Length(1, 200)])
    user_avatar = FileField('Avatar')

    def validate_user_avatar(self, field):
        """Validate user_avatar.

        This function shouldn't be necessary, but the Regexp validator does
        not work as advertised for FileFields.

        Args:
            field (object): Field to validate (user_avatar).

        Raises:
            ValidationError: When field is not a valid image.
        """
        file_name = field.data.filename
        if file_name and not AVATAR_RE.match(file_name):
            raise ValidationError("File must be an image")

    def get_post_invalid_message(self):
        """Get the default error message for a invalid post request.

        Returns:
            str: Message including invalid field names.
        """
        field_to_label = {'user_name': 'Name', 'user_avatar': 'Avatar'}

        error_fields = sorted(self.errors.keys())
        field_or_fields = 'fields' if len(error_fields) > 1 else 'field'

        return "Invalid data provided for {0}: {1}".format(
            field_or_fields,
            ', '.join(map(lambda f: field_to_label[f], error_fields)))
