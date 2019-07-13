import json

from unittest.mock import patch

from app import models


def test_index(test_app):
    client = test_app.test_client()
    response = client.get('/api/home')

    assert response.status_code == 200
    assert json.loads(response.data) == {"index": "home"}


def test_task(test_app):

    with patch("app.api.start_task"):
        client = test_app.test_client()
        resp = client.post("/api/task/start")

        task_uuid = json.loads(resp.data)["task_id"]
        exp_task_uuid = models.Task.query.all()[0].uuid

        assert task_uuid == exp_task_uuid
