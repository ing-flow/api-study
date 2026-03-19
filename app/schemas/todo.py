from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    text: str
    completed: bool = False

class TodoResponse(Todo):
    id: int