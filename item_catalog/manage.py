"""Manage tech_quote application."""

from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager, Shell, Server
from flask.ext.script.commands import Clean, ShowUrls

from _db_manage import MANAGER as database_manager
from tech_quote.app import create_app
from tech_quote.database import db

APP = create_app()
MIGRATE = Migrate(APP, db)
MANAGER = Manager(APP)


def _make_context():
    """Make context with access to the application and database."""
    return {'app': APP, 'db': db}


MANAGER.add_command('db', database_manager)
MANAGER.add_command("clean", Clean())
MANAGER.add_command("migrate", MigrateCommand)
MANAGER.add_command('serve', Server())
MANAGER.add_command('shell', Shell(make_context=_make_context))
MANAGER.add_command("urls", ShowUrls())

if __name__ == '__main__':
    MANAGER.run()
