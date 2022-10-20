from core.setup import create_app
from flask_jwt_extended import JWTManager

app = create_app(__name__)

app.config["JWT_SECRET_KEY"] = "password_super_secreta_ja_ja_ja"
jwt = JWTManager(app)

if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0")
    app.run(debug=True)
