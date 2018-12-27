import http
from flask import jsonify, make_response


def json_response(data=None, status=http.HTTPStatus.OK, headers=None):
    """Generate json response with given payload, status and headers."""
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = 'application/json'
    return make_response(jsonify(data), status, headers)
