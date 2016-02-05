"""Define models for tech_quote roles,users."""

from datetime import datetime

from flask.ext.login import UserMixin

from tech_quote.database import Column, Model, db


class User(UserMixin, Model):

    """A user of the TQ app."""

    __tablename__ = 'tq_user'

    user_id = Column(db.Integer, primary_key=True)

    user_email = Column(db.String(80), unique=True, nullable=False)
    user_name = Column(db.String(70), nullable=True)
    user_avatar_url = Column(db.String(200), nullable=False)
    user_github_id = Column(db.Integer, unique=True, nullable=False)
    user_github_login = Column(db.String(80), unique=True, nullable=False)
    user_created = Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    user_is_active = Column(db.Boolean(), default=False)
    user_is_admin = Column(db.Boolean(), default=False)

    def __init__(self, **kwargs):
        """Create instance of User.

        Args:
            **kwargs: Keyword arguments for creating a User.
        """
        super(User, self).__init__(**kwargs)

    @classmethod
    def by_github_id(cls, github_id):
        """Get a user by a specified github_id.

        Args:
            github_id (str): GitHub login id of user to get.

        Returns:
            object: An instance of `User` with specified id or None.
        """
        return cls.query.filter_by(user_github_id=github_id).one_or_none()

    def get_id(self):
        """Get unicode id that uniquely identifies a User.

        Returns:
            unicode: Id used to identify a `User`.
        """
        return unicode(self.user_id)

    def __repr__(self):
        """Represent User instance as a string.

        Returns:
            str: Representation of a User object.
        """
        return '<User({0}, {1})>'.format(
            self.user_email, self.user_github_login)


class Role(Model):

    """A role for a TQ user."""

    __tablename__ = 'role'

    role_id = Column(db.Integer, primary_key=True)

    role_name = Column(db.String(80), unique=True, nullable=False)

    user_id = Column(db.Integer, db.ForeignKey('tq_user.user_id'))
    user = db.relationship(User, backref='role')

    def __init__(self, **kwargs):
        """Create instance of Role.

        Args:
            **kwargs: Keyword arguments for creating a Role.
        """
        super(Role, self).__init__(**kwargs)

    def __repr__(self):
        """Represent Role instance as a string.

        Returns:
            str: Representation of a Role object.
        """
        return '<Role({0})>'.format(self.role_name)
