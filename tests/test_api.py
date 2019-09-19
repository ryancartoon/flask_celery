import json

# from unittest.mock import patch

# from app import models
from app.api import add_task


def test_tasks(test_app):
    expect_tasks = [add_task(), add_task()]

    client = test_app.test_client()
    resp = client.get("/api/tasks")

    assert [t["uuid"]
            for t in json.loads(resp.data)] == [t.uuid for t in expect_tasks]


def test_task(test_app):
    task = add_task()

    client = test_app.test_client()
    resp = client.get("/api/tasks/" + task.uuid)

    assert task.uuid == resp.json["uuid"]
