"""Setup the tech_quote database (tq)."""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql+psycopg2:///tq', echo=True)
session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = session.query_property()


def init_db():
    """Setup the (tq) database."""
    import tech_quote.models
    Base.metadata.create_all(bind=engine)
