from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity


class Product(Resource):

    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        return {"hola": "mundo", "querying_user": current_user_id}
