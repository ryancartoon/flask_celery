from flask import Blueprint, jsonify, current_app
from uuid import uuid4

from .task import start_task
from .models import Task
from . import db

api = Blueprint('api', __name__)


@api.route('/home')
def index():
    return jsonify({"index": "home"})


@api.route('/tasks')
def tasks():
    tasks = db.session.query(Task).all()

    return jsonify({
        "task_uuids": [{
            "uuid": task.uuid,
            "status": task.status
        } for task in tasks]
    })


@api.route('/task/start')
def start():
    task = Task()
    task.uuid = str(uuid4())
    task.status = 'running'

    db.session.add(task)
    db.session.commit()

    start_task.apply_async(None, None, task.uuid)

    return jsonify({"task_id": task.uuid})


@api.route('/task/<task_uuid>/status')
def task_status(task_uuid):
    task = {}
    task_db = current_app.db.session.query(uuid=task_uuid).first_or_404()

    task['uuid'] = task_uuid
    task['status'] = task_db.status

    return jsonify(task)
