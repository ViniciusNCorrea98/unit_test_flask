from flask import Flask
import os
from flask_migrate import Migrate
from model import configure as config_db


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(app.root_path, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from serealizer import configure as config_ma

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    from .books import bp_books
    app.register_blueprint(bp_books)

    return app