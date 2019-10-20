from flask_restplus import Api, Resource, fields, abort
from uuid import uuid4

from .task import start_task
from . import models, db
from .constants import TaskStatus


api = Api(
    version='1.0',
    title='TASK API',
    description='task api',
)

ns = api.namespace('api', description='task api namespace')


def add_task(task_type):

    task = models.Task()

    task.uuid = str(uuid4())
    task.status = TaskStatus.running.value
    task.task_type = task_type

    db.session.add(task)
    db.session.commit()

    return task


class TaskStatusFields(fields.Raw):
    def format(self, value):
        return TaskStatus(value).name


task_response_model = api.model('task_response', {
    "uuid": fields.String(description="task id", required=True),
    "status": TaskStatusFields(description="task status", required=True),
    "task_type": fields.String(description="task type", required=True, default="not defined"),
    "created_at": fields.DateTime(description="time task was created", required=True),
})


task_request_model = api.model('task_request', {
    "task_type": fields.String,
})


@ns.route('/tasks')
class TaskList(Resource):
    @api.doc('get all tasks')
    @api.marshal_list_with(task_response_model, code=200)
    def get(self):
        return db.session.query(models.Task).all(), 200

    @api.doc(responses={
        201: 'Task is started',
        400: 'Validation Error',
    })
    @api.expect(task_request_model, validate=True)
    @api.marshal_with(task_response_model, code=201)
    def post(self):
        task_type = api.payload["task_type"]

        if task_type not in ["type1", "type2"]:
            abort(400, "task type is in correct.", task_type=task_type)

        task = add_task(task_type)
        start_task.apply_async(None, None, task.uuid)

        return task, 201


@ns.route('/tasks/<task_id>')
class Task(Resource):
    @api.doc('get a task')
    @api.marshal_with(task_response_model, code=200)
    def get(self, task_id):
        task = db.session.query(models.Task).filter_by(uuid=task_id).one()

        return task, 200
