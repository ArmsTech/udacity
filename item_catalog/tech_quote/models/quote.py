"""Define models for tech_quote quotes."""

from datetime import datetime

from tech_quote.database import Column, Model, db
from tech_quote.models.user import User


class Author(Model):

    """An author in the TQ app."""

    __tablename__ = 'author'

    author_id = Column(db.Integer, primary_key=True)
    author_name = Column(db.String(70), nullable=False)
    author_bio = Column(db.String(200), nullable=False)
    author_created = Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        """Create instance of Author.

        Args:
            **kwargs: Keyword arguments for creating an Author.
        """
        super(Author, self).__init__(**kwargs)

    def __repr__(self):
        """Represent Author instance as a string.

        Returns:
            str: Representation of an Author object.
        """
        return '<Author author_id={0}, author_name={1}>'.format(
            self.author_id, self.author_name)


class Category(Model):

    """A category in the TQ app."""

    __tablename__ = 'category'

    category_id = Column(db.Integer, primary_key=True)
    category_name = Column(db.String(70), nullable=False)
    category_description = Column(db.Text, nullable=False)
    category_icon_url = Column(db.String(200), nullable=False)

    def __init__(self, **kwargs):
        """Create instance of Category.

        Args:
            **kwargs: Keyword arguments for creating an Category.
        """
        super(Category, self).__init__(**kwargs)

    def __repr__(self):
        """Represent Category instance as a string.

        Returns:
            str: Representation of a Category object.
        """
        return '<Category category_id={0}, category_name={1}>'.format(
            self.category_id, self.category_name)


class Quote(Model):

    """A quote in the TQ app."""

    __tablename__ = 'quote'

    quote_id = Column(db.Integer, primary_key=True)
    quote_text = Column(db.Text, nullable=False)
    quote_source = Column(db.String(200), nullable=False)
    quote_created = Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    author_id = Column(
        db.Integer, db.ForeignKey('author.author_id'), nullable=False)
    author = db.relationship(Author)
    category_id = Column(
        db.Integer, db.ForeignKey('category.category_id'), nullable=False)
    category = db.relationship(Category)
    user_id = Column(
        db.Integer, db.ForeignKey('tq_user.user_id'), nullable=False)
    user = db.relationship(User, backref='quote')

    def __init__(self, **kwargs):
        """Create instance of Quote.

        Args:
            **kwargs: Keyword arguments for creating a Quote.
        """
        super(Quote, self).__init__(**kwargs)

    def is_owned_by(self, user):
        """Whether quote is owned by provided user object.

        Args:
            user (object): User to check against.

        Returns:
            bool: Whether quote is owned by `user`.
        """
        return unicode(self.user_id) == user.get_id()

    @classmethod
    def get_quotes_with_pagination(cls, page, **kwargs):
        """Get a number of quotes for a specified page.

        Args:
            page (int): Page of quotes to get.
            **kwargs: Filters to be applied to query.

        Returns:
            object: Pagination object to get quotes for page.
        """
        quotes_per_page = db.get_app().config['QUOTES_PER_PAGE']
        return cls.query.filter_by(**kwargs).order_by(
            cls.quote_created.desc()).paginate(page, quotes_per_page)

    def __repr__(self):
        """Represent Quote instance as a string.

        Returns:
            str: Representation of a Quote object.
        """
        return '<Quote quote_id={0}, quote_text={1}>'.format(
            self.quote_id, self.quote_text)
