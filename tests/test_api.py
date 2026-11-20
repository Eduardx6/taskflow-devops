import pytest

from app.main import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}


def test_create_and_get_task(client):
    r = client.post("/tasks", json={"title": "Estudar DevOps"})
    assert r.status_code == 201
    task = r.get_json()
    assert task["status"] == "pendente"
    r = client.get(f"/tasks/{task['id']}")
    assert r.status_code == 200
    assert r.get_json()["title"] == "Estudar DevOps"


def test_create_task_without_title_returns_400(client):
    assert client.post("/tasks", json={}).status_code == 400
    assert client.post("/tasks", json={"title": "   "}).status_code == 400


def test_list_and_filter_by_status(client):
    a = client.post("/tasks", json={"title": "A"}).get_json()
    client.post("/tasks", json={"title": "B"})
    client.patch(f"/tasks/{a['id']}", json={"status": "concluida"})
    assert len(client.get("/tasks").get_json()) == 2
    done = client.get("/tasks?status=concluida").get_json()
    assert [t["title"] for t in done] == ["A"]


def test_update_task_status(client):
    t = client.post("/tasks", json={"title": "X"}).get_json()
    r = client.patch(f"/tasks/{t['id']}", json={"status": "em_andamento"})
    assert r.status_code == 200
    assert r.get_json()["status"] == "em_andamento"


def test_update_with_invalid_status_returns_400(client):
    t = client.post("/tasks", json={"title": "X"}).get_json()
    assert client.patch(f"/tasks/{t['id']}", json={"status": "foo"}).status_code == 400


def test_update_missing_task_returns_404(client):
    assert client.patch("/tasks/99", json={"status": "concluida"}).status_code == 404


def test_delete_task(client):
    t = client.post("/tasks", json={"title": "X"}).get_json()
    assert client.delete(f"/tasks/{t['id']}").status_code == 204
    assert client.get(f"/tasks/{t['id']}").status_code == 404
    assert client.delete(f"/tasks/{t['id']}").status_code == 404


def test_get_missing_task_returns_404(client):
    assert client.get("/tasks/42").status_code == 404
