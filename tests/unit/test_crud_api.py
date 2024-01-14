from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)

user_id = str(uuid.uuid4())


def test_root():
    response = client.get("/api/healthchecker")
    assert response.status_code == 200
    assert response.json() == {"message": "The API is live"}


def test_create_user():
    sample_payload = {
        "id": user_id,
        "first_name": "PLACEHOLDER",
        "last_name": "PLACEHOLDER",
        "address": "PLACEHOLDER",
        "activated": False,
        "created_at": "2023-03-17T00:04:32",
    }

    response = client.post("/api/users/", json=sample_payload)
    assert response.status_code == 201
    assert response.json()["status"] == "success"
    assert response.json()["user"]["id"] == sample_payload["id"]
    assert response.json()["user"]["first_name"] == sample_payload["first_name"]

def test_get_user():
    response = client.get(f"/api/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert response.json()["user"]["id"] == user_id

def test_update_user():
    sample_payload = {
        "id": user_id,
        "first_name": "UPDATED",
        "last_name": "UPDATED",
        "address": "UPDATED",
        "activated": True,
        "created_at": "2023-03-17T00:04:32",
    }

    response = client.patch(f"/api/users/{user_id}", json=sample_payload)
    assert response.status_code == 202
    assert response.json()["status"] == "success"
    assert response.json()["user"]["id"] == sample_payload["id"]
    assert response.json()["user"]["first_name"] == sample_payload["first_name"]

def test_delete_user():
    response = client.delete(f"/api/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == {
        "status": "success",
        "message": "user deleted successfully",
    }

def test_get_user_not_found():
    user_id = str(uuid.uuid4())
    response = client.get(f"/api/users/{user_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == f"No User with this id: `{user_id}` found"