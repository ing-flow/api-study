from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

app = FastAPI()

# ---- データモデル ----

class Todo(BaseModel):
    text: str
    completed: bool = False

class TodoResponse(Todo):
    id: str

# ---- 疑似DB ----

todos: List[dict] = []

# ---- 取得 ----

@app.get("/todos", response_model=List[TodoResponse])
def get_todos():
    return todos

# ---- 作成 ----

@app.post("/todos", response_model=TodoResponse)
def create_todo(todo: Todo):
    new_todo = {
        "id": str(uuid.uuid4()),
        "text": todo.text,
        "completed": todo.completed
    }
    todos.append(new_todo)
    return new_todo

# ---- 更新（PUT: 全置換）----

@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: str, updated: Todo):
    for t in todos:
        if t["id"] == todo_id:
            t["text"] = updated.text
            t["completed"] = updated.completed
            return t
    raise HTTPException(status_code=404, detail="Not found")

# ---- 部分更新（PATCH）----

@app.patch("/todos/{todo_id}", response_model=TodoResponse)
def patch_todo(todo_id: str, updated: Todo):
    for t in todos:
        if t["id"] == todo_id:
            if updated.text is not None:
                t["text"] = updated.text
            t["completed"] = updated.completed
            return t
    raise HTTPException(status_code=404, detail="Not found")

# ---- 削除 ----

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):
    for i, t in enumerate(todos):
        if t["id"] == todo_id:
            todos.pop(i)
            return {"message": "deleted"}
    raise HTTPException(status_code=404, detail="Not found")