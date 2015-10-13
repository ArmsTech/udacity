"""Manage tech_quote application."""

from flask.ext.script import Manager, Shell, Server, prompt_bool
from flask.ext.script.commands import Clean, ShowUrls

from tech_quote.app import create_app
from tech_quote.database import db

APP = create_app()
MANAGER = Manager(APP)


def _make_context():
    """Make context with access to the application and database."""
    return {'app': APP, 'db': db}


@MANAGER.command
def create_tables():
    """Create tech_quote database tables."""
    db.create_all()


@MANAGER.command
def drop_tables():
    """Drop tech_quote database tables."""
    if prompt_bool("Drop all database tables?"):
        db.drop_all()
    else:
        import sys
        sys.exit(1)


MANAGER.add_command('server', Server())
MANAGER.add_command('shell', Shell(make_context=_make_context))
MANAGER.add_command("urls", ShowUrls())
MANAGER.add_command("clean", Clean())

if __name__ == '__main__':
    MANAGER.run()
