import pytest
import json

from unittest.mock import patch

from app import create_app, db
from app import models


@pytest.fixture
def app():
    app = create_app('testing')
    app_context = app.app_context()
    app_context.push()
    db.create_all()

    yield app

    db.session.remove()
    db.drop_all()
    app_context.pop()


def test_index(app):
    client = app.test_client()
    response = client.get('/api/home')

    assert response.status_code == 200
    assert json.loads(response.data) == {"index": "home"}


def test_task(app):

    with patch("app.api.start_task"):
        client = app.test_client()
        resp = client.post("/api/task/start")

        task_uuid = json.loads(resp.data)["task_id"]
        exp_task_uuid = models.Task.query.all()[0].uuid

        assert task_uuid == exp_task_uuid
