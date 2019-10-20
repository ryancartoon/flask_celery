from datetime import datetime

from . import db



class Base(object):
    created_at = db.Column(db.DateTime, default=datetime.now())


class Task(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)
    task_type = db.Column(db.String(10))

    def __repr__(self):
        return '<UUID %r>' % self.uuid
