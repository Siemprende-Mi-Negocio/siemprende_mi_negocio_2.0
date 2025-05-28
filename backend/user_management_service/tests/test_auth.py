import pytest
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

def test_register_and_login():
    response = client.post("/api/v1/auth/register", json={"email": "test@example.com", "password": "secret"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

    response = client.post("/api/v1/auth/login", json={"email": "test@example.com", "password": "secret"})
    assert response.status_code == 200
    assert "access_token" in response.json()

    response = client.post("/api/v1/auth/login", json={"email": "test@example.com", "password": "wrong"})
    assert response.status_code == 401
