from fastapi import APIRouter, HTTPException

from controllers.user_controller import register_user, authenticate_user
from models.user_model import UserCreate, UserLogin, User

router = APIRouter()


@router.post("/register", response_model=User)
def register(user: UserCreate):
    try:
        return register_user(user)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.post("/login")
def login(credentials: UserLogin):
    token = authenticate_user(credentials)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}
