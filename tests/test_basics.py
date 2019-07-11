import pytest

from flask import current_app

from app import create_app, db, app_name


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


def test_app_exists(app):
    assert current_app.name is app_name


def test_app_is_testing(app):
    assert current_app.config['TESTING'] is True
