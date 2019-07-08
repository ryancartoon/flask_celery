import os

from . import create_app_celery
from .celery import make_celery

app = create_app_celery(os.getenv('FLASK_CONFIG') or 'default')
celery_app = make_celery(app)


@celery_app.task(bind=True)
def start_task(self):
    with celery_app.app_context():
        app_name = celery_app.app_name
        print('app name is %s' % app_name)

    return app_name
