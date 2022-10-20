from flask import Blueprint
from flask_restful import Api

from core.routes.product.product import Product

product_blueprint = Blueprint("product", __name__, url_prefix="/products")

product_api = Api(product_blueprint)


product_api.add_resource(Product, "/")
