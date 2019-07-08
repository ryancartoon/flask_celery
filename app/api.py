from flask import Blueprint, jsonify, current_app
from uuid import uuid4
from .task import start_task
from .model import Task

api = Blueprint('api', __name__)


@api.route('/task/start')
def start():
    db = current_app.db
    uuid = uuid4()
    task = Task()

    task.uuid = uuid
    task.status = 'running'
    db.session.add(task)
    db.session.commit()

    task = start_task.delay()

    return jsonify({"task_id": task.uuid})


@api.route('/home')
def index():
    return jsonify({"index": "home"})


@api.route('/task/<task_uuid>/status')
def task_status(task_uuid):
    task = {}
    task_db = current_app.db.session.query(uuid=task_uuid).first_or_404()

    task['uuid'] = task_uuid
    task['status'] = task_db.status

    return jsonify(task)
