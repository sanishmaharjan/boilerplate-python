#!/usr/bin/env python3
"""
Documentation

See also https://www.python-boilerplate.com/flask
"""
import os
import http
import traceback
from time import time
from logzero import logger
from flask_cors import CORS
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, request, g
from controller import controller_blueprint


def create_app(config=None):
    app = Flask(__name__)

    # See http://flask.pocoo.org/docs/latest/config/
    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})

    # Setup cors headers to allow all domains
    # https://flask-cors.readthedocs.io/en/latest/
    CORS(app)
    app.register_blueprint(controller_blueprint, url_prefix='')

    @app.before_request
    def before_request():
        """
            A function to run before each request.
        """

        logger.debug('Request [{request_method}] : {request_url}'
                     .format(request_method=request.method, request_url=request.base_url))
        g.start_time = time()

    @app.after_request
    def after_request(response):
        """
            A function to run after each request.
        """

        execution_time = time() - g.start_time
        logger.debug('Request completion time: {execution_time}'.format(execution_time=execution_time))

        return response

    @app.errorhandler(Exception)
    def exceptions(error):
        ts = datetime.now().strftime('[%Y-%b-%d %H:%M]')
        tb = traceback.print_stack(limit=5)
        path = "?".join(
            [request.path,
             request.query_string]) if request.query_string else request.path
        logger.error('%s %s %s %s %s 500 INTERNAL SERVER ERROR\n%s',
                     ts, request.remote_addr, request.method, request.scheme, path, tb)

        return 'Internal Server Error', http.HTTPStatus.INTERNAL_SERVER_ERROR

    # Definition of the routes. Put them into their own file. See also
    # Flask Blueprints: http://flask.pocoo.org/docs/latest/blueprints
    @app.route("/")
    def main():
        return "Boiler-Plate Python Application"

    return app


if __name__ == "__main__":
    load_dotenv(verbose=True)
    port = int(os.environ.get("PORT", 8000))
    app = create_app()
    app.run(host="0.0.0.0", port=port)
