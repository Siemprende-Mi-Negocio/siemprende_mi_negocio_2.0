from typing import Dict, Optional
import hashlib
import secrets

from models.user_model import UserCreate, UserLogin, User

_fake_users: Dict[str, Dict[str, str]] = {}
_user_id_seq = 1


def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(data: UserCreate) -> User:
    global _user_id_seq
    if data.email in _fake_users:
        raise ValueError("User already exists")
    hashed = _hash_password(data.password)
    record = {"id": _user_id_seq, "email": data.email, "password": hashed}
    _fake_users[data.email] = record
    _user_id_seq += 1
    return User(id=record["id"], email=record["email"])


def authenticate_user(credentials: UserLogin) -> Optional[str]:
    record = _fake_users.get(credentials.email)
    if not record:
        return None
    if record["password"] != _hash_password(credentials.password):
        return None
    return secrets.token_hex(16)
