from flask_restful import Resource


class Product(Resource):

    def get(self):

        return {"hola": "mundo"}