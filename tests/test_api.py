import json

from unittest.mock import patch

from app import models
from app.api import add_task


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


def test_tasks(test_app):
    expect_tasks = [add_task(), add_task()]

    client = test_app.test_client()
    resp = client.get("/api/tasks")

    assert [t["uuid"] for t in json.loads(resp.data)["tasks"]].sort() \
        == expect_tasks.sort()
