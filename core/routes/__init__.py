from core.routes.product.blueprint import product_api, product_blueprint
from core.routes.user.blueprint import user_api, user_blueprint

blueprints = [
    product_blueprint,
    user_blueprint,
]

apis = [
    product_api,
    user_api,
]