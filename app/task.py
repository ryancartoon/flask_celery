import os

from flask import current_app

from . import create_app_celery, db
from .celery import make_celery
from .constants import TaskStatus
from .models import Task

app = create_app_celery(os.getenv('FLASK_CONFIG') or 'default')
celery_app = make_celery(app)


@celery_app.task(bind=True)
def start_task(self):
    task_uuid = self.request.id
    task_db = db.session.query(Task).filter_by(uuid=task_uuid)
    task_db.update({"status": TaskStatus.completed.value})
    db.session.commit()
    print('app name is %s' % current_app.name)
    print('task: %s is done.' % task_uuid)
