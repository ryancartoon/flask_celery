import os

from flask_migrate import Migrate, upgrade

from app import create_app, db
from app.models import Task

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Task=Task)


@app.cli.command()
def deploy():
    upgrade()
