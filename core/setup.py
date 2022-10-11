from flask import Flask, request
from flask_restful import Resource, Api
from core.models import engine
from datetime import datetime, timedelta
import simplejson as json

from core.routes import apis, blueprints


def create_app(name):
    app = Flask(name)
    api = Api(app)

    add_json_representation(app, api)
    for domain_api in apis:
        add_json_representation(app, domain_api)
    for domain_blueprint in blueprints:
        app.register_blueprint(domain_blueprint)

    return app


def add_json_representation(app, api):
    @api.representation("application/json")
    def output_json(data, code, headers=None):
        if code in (400, 401, 403, 404, 500):
            response_format = json.dumps({"error": data, "time": str(datetime.now())})
        else:
            response_format = json.dumps({"data": data, "time": str(datetime.now())})
        resp = app.make_response(response_format)
        resp.status_code = code
        resp.headers.extend(headers or {})
        return resp

    return api
