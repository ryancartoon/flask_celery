import pytest

from app import create_app, db


@pytest.fixture
def test_app():
    app = create_app("testing")
    app_context = app.app_context()
    app_context.push()
    db.create_all()

    yield app

    db.session.remove()
    db.drop_all()
    app_context.pop()
