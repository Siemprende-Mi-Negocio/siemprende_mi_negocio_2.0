from flask import Blueprint, jsonify, request
from controllers.auth_controller import register_user, login_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/register")
def register():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "username and password required"}), 400
    response, status = register_user(username, password)
    return jsonify(response), status


@auth_bp.post("/login")
def login():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "username and password required"}), 400
    response, status = login_user(username, password)
    return jsonify(response), status
