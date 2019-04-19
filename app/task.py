from . import create_app
from .celery import make_celery


app = create_app('default')
celery_app = make_celery(app)


@celery_app.task()
def add(a, b):
    return a + b
