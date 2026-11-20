"""TaskFlow API - API REST simples para gerenciamento de tarefas."""
from flask import Flask, jsonify, request

VALID_STATUS = {"pendente", "em_andamento", "concluida"}


def create_app() -> Flask:
    app = Flask(__name__)
    tasks: dict[int, dict] = {}
    counter = {"next_id": 1}

    @app.get("/health")
    def health():
        return jsonify(status="ok"), 200

    @app.get("/tasks")
    def list_tasks():
        status = request.args.get("status")
        items = list(tasks.values())
        if status:
            items = [t for t in items if t["status"] == status]
        return jsonify(items), 200

    @app.post("/tasks")
    def create_task():
        data = request.get_json(silent=True) or {}
        title = (data.get("title") or "").strip()
        if not title:
            return jsonify(error="O campo 'title' é obrigatório"), 400
        task = {"id": counter["next_id"], "title": title, "status": "pendente"}
        tasks[task["id"]] = task
        counter["next_id"] += 1
        return jsonify(task), 201

    @app.get("/tasks/<int:task_id>")
    def get_task(task_id: int):
        task = tasks.get(task_id)
        if task is None:
            return jsonify(error="Tarefa não encontrada"), 404
        return jsonify(task), 200

    @app.patch("/tasks/<int:task_id>")
    def update_task(task_id: int):
        task = tasks.get(task_id)
        if task is None:
            return jsonify(error="Tarefa não encontrada"), 404
        data = request.get_json(silent=True) or {}
        status = data.get("status")
        if status not in VALID_STATUS:
            return jsonify(error="Status inválido"), 400
        task["status"] = status
        return jsonify(task), 200

    @app.delete("/tasks/<int:task_id>")
    def delete_task(task_id: int):
        if tasks.pop(task_id, None) is None:
            return jsonify(error="Tarefa não encontrada"), 404
        return "", 204

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
