#!/usr/bin/python3

"""index """

from api.v1.views import from api.v1.views
from flask import jsonify

app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """return json """
    return jsonify(status="OK")
