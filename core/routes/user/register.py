from flask import request
from flask_restful import Resource

from core.models.user.user_model import UserModel
from core.models import session
import hashlib


class Register(Resource):

    def post(self):
        payload = request.get_json()

        name = payload.get("name")
        email = payload.get("email")
        password = hashlib.md5(payload.get("password").encode())

        user = UserModel(
            user_name=name,
            user_email=email,
            user_password=password.hexdigest()
        )
        session.add(user)
        session.commit()

        return {
            "id": user.user_id
        }
