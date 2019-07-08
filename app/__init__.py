from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

APP_NAME = 'FLASK_CELERY_DEMO'

db = SQLAlchemy()


def create_app(config_name):
    app = _create_app(config_name)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app


def create_app_celery(config_name):
    app = _create_app(config_name)

    return app


def _create_app(config_name):
    app = Flask(APP_NAME)
    app.config.from_object(config[config_name])

    db.init_app(app)

    return app
