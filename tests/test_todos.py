def test_create_todo_success(client):
    response = client.post(
        "/todos",
        json={
            "title": "Test todo",
            "description": "test",
            "is_done": False
        }
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test todo"


def test_create_todo_validation_fail(client):
    response = client.post(
        "/todos",
        json={
            "title": "",  # invalid
            "description": "test"
        }
    )
    assert response.status_code == 422


def test_get_todo_not_found(client):
    response = client.get("/todos/999999")
    assert response.status_code == 404