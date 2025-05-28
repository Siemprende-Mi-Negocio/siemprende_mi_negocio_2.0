from fastapi import FastAPI, HTTPException

from routes.user_routes import router as user_router

app = FastAPI(title="User Management Service", version="1.0.0")

app.include_router(user_router, prefix="/api/v1/auth")

@app.get("/healthz")
def health() -> dict:
    return {"status": "ok"}
