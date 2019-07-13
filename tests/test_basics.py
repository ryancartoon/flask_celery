
from flask import current_app

from app import app_name


def test_app_exists(test_app):
    assert current_app.name is app_name


def test_app_is_testing(test_app):
    assert current_app.config['TESTING'] is True
