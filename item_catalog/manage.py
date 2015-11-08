"""Manage tech_quote application."""

from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager, Shell, Server, prompt_bool
from flask.ext.script.commands import Clean, ShowUrls

from tech_quote.app import create_app
from tech_quote.database import db

APP = create_app()
MIGRATE = Migrate(APP, db)
MANAGER = Manager(APP)
DB_MANAGER = Manager(
    usage="python manage.py db <argument>",
    description="Manage database operations")


@DB_MANAGER.command
def create():
    """Create tech_quote database tables."""
    db.create_all()


@DB_MANAGER.command
def drop():
    """Drop tech_quote database tables."""
    if prompt_bool("Drop all database tables?"):
        db.drop_all()
    else:
        import sys
        sys.exit(1)


@DB_MANAGER.command
def recreate():
    """Recreate database (drop then create)."""
    drop()
    create()


def _make_context():
    """Make context with access to the application and database."""
    return {'app': APP, 'db': db}


MANAGER.add_command('db', DB_MANAGER)
MANAGER.add_command("clean", Clean())
MANAGER.add_command("migrate", MigrateCommand)
MANAGER.add_command('serve', Server())
MANAGER.add_command('shell', Shell(make_context=_make_context))
MANAGER.add_command("urls", ShowUrls())

if __name__ == '__main__':
    MANAGER.run()
