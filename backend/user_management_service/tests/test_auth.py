import pytest

from app import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_register_and_login(client):
    res = client.post("/api/v1/users/register", json={"username": "alice", "password": "secret"})
    assert res.status_code == 201

    res = client.post("/api/v1/users/login", json={"username": "alice", "password": "secret"})
    assert res.status_code == 200
