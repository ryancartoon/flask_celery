from flask import jsonify

from .api import api


@api.route('/hello')
def hello():
    from .task import show_app_name
    show_app_name.delay()
    return jsonify({"hello": "world"})
