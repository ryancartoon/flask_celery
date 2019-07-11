import pytest

from app import create_app, db
from app.models import Task


@pytest.fixture
def app():
    app = create_app('testing')
    app_context = app.app_context()
    app_context.push()
    db.create_all()
    Task.insert_roles()

    yield app

    db.session.remove()
    db.drop_all()
    app_context.pop()


# @pytest.fixture
# def client(app):
#     return app.test_client()
