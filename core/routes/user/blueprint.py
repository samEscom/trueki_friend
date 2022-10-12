from flask import Blueprint
from flask_restful import Api

from core.routes.user.register import Register

user_blueprint = Blueprint("user", __name__, url_prefix="/user")
user_api = Api(user_blueprint)

user_api.add_resource(Register, "/register")
