"""Define models for tech_quote database (tq)."""

from datetime import datetime

from tech_quote.extensions import db

Column = db.Column


class CRUDMixin(object):

    """Add convenience methods for CRUD operations."""

    @classmethod
    def create(cls, **kwargs):
        """Create."""
        instance = cls(**kwargs)
        return instance._save()

    def update(self, commit=True, **kwargs):
        """Update."""
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self._save() or self

    def delete(self, commit=True):
        """Delete."""
        db.session.delete(self)
        return commit and db.session.commit()

    def _save(self, commit=True):
        """Commit (save) if requested."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self


class Model(CRUDMixin, db.Model):
    """Base db.Model class with a CRUD mixin."""
    __abstract__ = True


class Author(Model):

    """Represent an author table in tq."""

    __tablename__ = 'author'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(60), nullable=False)
    biography = Column(db.Text, nullable=False)
    website = Column(db.String(60), nullable=False)
    created = Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        """Custom initialization for Author."""
        super(Author, self).__init__(**kwargs)

    def __repr__(self):
        """Compute representation of an Author object."""
        return '<Author id={0}, name={1}>'.format(self.id, self.name)


class Category(Model):

    """Represent an category table in tq."""

    __tablename__ = 'category'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(60), nullable=False)
    description = Column(db.Text, nullable=False)
    icon = Column(db.LargeBinary, nullable=False)

    def __init__(self, **kwargs):
        """Custom initialization for category."""
        super(Category, self).__init__(**kwargs)

    def __repr__(self):
        """Compute representation of an category object."""
        return '<Category id={0}, name={1}>'.format(self.id, self.name)


class Quote(Model):

    """Represent a quote table in tq."""

    __tablename__ = 'quote'

    id = Column(db.Integer, primary_key=True)
    text = Column(db.Text, nullable=False)
    source = Column(db.String(60), nullable=False)
    created = Column(db.DateTime, nullable=False, default=datetime.utcnow)

    author_id = Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship(Author)
    category_id = Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship(Category)

    def __init__(self, **kwargs):
        """Custom initialization for Quote."""
        super(Quote, self).__init__(**kwargs)

    def __repr__(self):
        """Compute representation of an Quote object."""
        return '<Quote id={0}, text={1}>'.format(self.id, self.text)
