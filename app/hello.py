from flask import jsonify

from .api import api
from .task import show_app_name


@api.route('/hello')
def hello():
    show_app_name.delay()
    return jsonify({"hello": "world"})
