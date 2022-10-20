from flask import request
from flask_restful import Resource

from core.models.user.user_model import UserModel
from core.models import session
from core.utils.users import str_to_hash
from flask_jwt_extended import create_access_token


class Login(Resource):

    def post(self):
        payload = request.get_json()

        email = payload.get("email")
        password = str_to_hash(payload.get("password"))

        user: UserModel = session.query(UserModel).filter(
            UserModel.user_email == email,
            UserModel.user_password == password
        ).first()

        if user is None:
            return {"error": "error on user or password"}

        access_token = create_access_token(identity=user.user_id)
        return {
            "user_id": user.user_id,
            "user_name": user.user_name,
            "token": access_token,
        }
