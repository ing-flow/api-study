
def test_create_todo(client):

    response = client.post(
        "/todos",
        json={
            "text": "pytest todo",
            "completed": False
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["text"] == "pytest todo"
    assert data["completed"] == False
    assert "id" in data

def test_get_todos_empty(client):

    response = client.get("/todos")

    assert response.status_code == 200
    assert response.json() == []


def test_get_todos_after_create(client):

    client.post(
        "/todos",
        json={
            "text": "todo1",
            "completed": False
        }
    )

    response = client.get("/todos")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["text"] == "todo1"