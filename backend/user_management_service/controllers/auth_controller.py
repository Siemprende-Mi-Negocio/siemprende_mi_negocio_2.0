from typing import Dict, Tuple

from models.user_model import User

users_db: Dict[str, User] = {}


def register_user(username: str, password: str) -> Tuple[Dict[str, str], int]:
    if username in users_db:
        return {"error": "User already exists"}, 400
    users_db[username] = User(username=username, password=password)
    return {"message": "User registered successfully"}, 201


def login_user(username: str, password: str) -> Tuple[Dict[str, str], int]:
    user = users_db.get(username)
    if user and user.password == password:
        return {"message": "Login successful"}, 200
    return {"error": "Invalid credentials"}, 401
