"""Define models for tech_quote database (tq)."""

from datetime import datetime

from sqlalchemy import (
    Column, DateTime, ForeignKey, Integer, LargeBinary, String, Text)
from sqlalchemy.orm import relationship

from tech_quote.database import Base


class Author(Base):

    """Represent an author table in tq."""

    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    biography = Column(Text, nullable=False)
    website = Column(String(60), nullable=False)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        """Custom initialization for Author."""
        super(Author, self).__init__(**kwargs)

    def __repr__(self):
        """Compute representation of an Author object."""
        return '<Author id={0}, name={1}>'.format(self.id, self.name)


class Category(Base):

    """Represent an category table in tq."""

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    description = Column(Text, nullable=False)
    icon = Column(LargeBinary, nullable=False)

    def __init__(self, **kwargs):
        """Custom initialization for category."""
        super(Category, self).__init__(**kwargs)

    def __repr__(self):
        """Compute representation of an category object."""
        return '<Category id={0}, name={1}>'.format(self.id, self.name)


class Quote(Base):

    """Represent a quote table in tq."""

    __tablename__ = 'quote'

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    source = Column(String(60), nullable=False)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)

    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship(Author)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

    def __init__(self, **kwargs):
        """Custom initialization for Quote."""
        super(Quote, self).__init__(**kwargs)

    def __repr__(self):
        """Compute representation of an Quote object."""
        return '<Quote id={0}, text={1}>'.format(self.id, self.text)
