from . import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<UUID %r>' % self.uuid
