from flask import jsonify, current_app
from flask_restplus import Api, Resource
from uuid import uuid4
from marshmallow import Schema, fields

from .task import start_task
from . import models, db

api = Api(version='1.0', title='Task API',
    description='A simple Task API',
)

def add_task():
    task = models.Task()
    task.uuid = str(uuid4())
    task.status = 'running'

    db.session.add(task)
    db.session.commit()

    return task


class TaskSchema(Schema):
    uuid = fields.Str()
    status = fields.Str()


@api.route('/tasks')
class TaskList(Resource):

    @api.doc('get all tasks')
    def get(self):
        schema = TaskSchema()
        tasks = db.session.query(models.Task).all()

        return schema.dump(tasks, many=True)

    @api.doc('start a task')
    def post(self):
        task = add_task()
        start_task.apply_async(None, None, task.uuid)

        schema = TaskSchema()
        return schema.dump(task)


@api.route('/tasks/<task_id>')
class Task(Resource):

    @api.doc('get a task')
    def get(self, task_id):
        schema = TaskSchema()
        task = db.session.query(models.Task).filter_by(uuid=task_id).one()

        return schema.dump(task)
