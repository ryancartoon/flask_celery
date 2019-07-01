from flask import Blueprint, jsonify
from .task import start_task

api = Blueprint('api', __name__)


@api.route('/start')
def start():
    task = start_task.delay()
    return jsonify({"task_id": task.id})


@api.route('/home')
def index():
    return jsonify({"index": "home"})
