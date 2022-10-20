from flask import Blueprint
from flask_restful import Api

from core.routes.user.register import Register
from core.routes.user.login import Login

user_blueprint = Blueprint("user", __name__, url_prefix="/user")
user_api = Api(user_blueprint)

user_api.add_resource(Register, "/register")
user_api.add_resource(Login, "/login")
