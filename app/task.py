import os
from flask import current_app

from . import create_app_celery
from .celery import make_celery


app = create_app_celery(os.getenv('FLASK_CONFIG') or 'default')
celery_app = make_celery(app)


@celery_app.task()
def start_task():
    name = current_app.name
    return name
