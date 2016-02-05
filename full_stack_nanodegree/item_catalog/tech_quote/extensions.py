"""Flask extensions (most of them) used by tech_quote."""

from flask.ext.login import LoginManager
login_manager = LoginManager()

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask.ext.migrate import Migrate
migrate = Migrate()

from flask.ext.assets import Environment
assets = Environment()

from flask.ext.uploads import IMAGES, UploadSet
avatars = UploadSet('avatars', IMAGES)
