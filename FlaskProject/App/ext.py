from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # orm
migrate = Migrate()  # 数据库迁移


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)
    DebugToolbarExtension(app)
