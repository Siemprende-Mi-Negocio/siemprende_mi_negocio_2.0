from flask import Flask
from routes.auth_routes import auth_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(auth_bp, url_prefix="/api/v1/users")
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080)
