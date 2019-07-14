from flask import Blueprint, jsonify, current_app
from uuid import uuid4

from .task import start_task
from . import models
from . import db

api = Blueprint('api', __name__)


def add_task():
    task = models.Task()
    task.uuid = str(uuid4())
    task.status = 'running'

    db.session.add(task)
    db.session.commit()

    return task.uuid


@api.route('/home')
def index():
    return jsonify({"index": "home"})


@api.route('/tasks')
def tasks():
    tasks = db.session.query(models.Task).all()

    return jsonify({
        "tasks": [{
            "uuid": task.uuid,
            "status": task.status
        } for task in tasks]
    })


@api.route('/task/start', methods=['POST'])
def start():

    task_uuid = add_task()
    start_task.apply_async(None, None, task_uuid)

    return jsonify({"task_id": task_uuid})


@api.route('/task/<task_uuid>/status')
def task_status(task_uuid):
    task = {}
    task_db = current_app.db.session.query(uuid=task_uuid).first_or_404()

    task['uuid'] = task_uuid
    task['status'] = task_db.status

    return jsonify(task)
