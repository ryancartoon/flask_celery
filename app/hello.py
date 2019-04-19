from flask import jsonify
from .api import api

from .task import add


@api.route('/hello')
def hello():
    a = 1
    b = 2
    result = add.delay(a, b)
    result.wait()
    return jsonify({"hello": "world"})
