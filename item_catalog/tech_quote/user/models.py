"""Define models for tech_quote roles,users."""

from datetime import datetime

from flask.ext.login import UserMixin

from tech_quote.database import Column, Model, db


class Role(Model):
    """A role for a tq user."""

    __tablename__ = 'role'

    role_id = Column(db.Integer, primary_key=True)
    role_name = Column(db.String(80), unique=True, nullable=False)

    user_id = Column(db.Integer, db.ForeignKey('user.user_id'))
    user = db.relationship('User', backref='role')

    def __init__(self, name, **kwargs):
        """Create instance for Role."""
        super(Role, self).__init__(name=name, **kwargs)

    def __repr__(self):
        """Represent Role instance as a string."""
        return '<Role({0})>'.format(self.name)


class User(UserMixin, Model):
    """A user of the tq app."""

    __tablename__ = 'user'

    user_id = Column(db.Integer, primary_key=True)
    user_email = Column(db.String(80), unique=True, nullable=False)
    user_first_name = Column(db.String(30), nullable=True)
    user_last_name = Column(db.String(30), nullable=True)
    user_created = Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    user_active = Column(db.Boolean(), default=False)
    user_is_admin = Column(db.Boolean(), default=False)

    def __init__(self, email, **kwargs):
        """Create instance for User."""
        super(User, self).__init__(email=email, **kwargs)

    @property
    def full_name(self):
        """Full user name."""
        return '{0} {1}'.format(self.user_first_name, self.user_last_name)

    def __repr__(self):
        """Represent User instance as a string."""
        return '<User({0})>'.format(self.email)
