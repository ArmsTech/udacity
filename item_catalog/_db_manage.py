"""Sub-manager for tech_quote database."""

from flask.ext.script import Manager, prompt_bool

from tech_quote.database import db

MANAGER = Manager(
    usage="python manage.py db <argument>",
    description="Manage database operations")


@MANAGER.command
def create():
    """Create tech_quote database tables."""
    db.create_all()


@MANAGER.command
def drop():
    """Drop tech_quote database tables."""
    if prompt_bool("Drop all database tables?"):
        db.drop_all()
    else:
        import sys
        sys.exit(1)


@MANAGER.command
def recreate():
    """Recreate database (drop then create)."""
    drop()
    create()
