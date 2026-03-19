from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.services.todo_service import TodoService
from app.schemas.todo import Todo, TodoResponse
from app.dependencies import get_todo_service
from app.core.logger import get_app_logger

logger = get_app_logger(__name__)

router = APIRouter()

@router.get("/todos", response_model=List[TodoResponse])
def list_todos(service: TodoService = Depends(get_todo_service)):

    logger.info("GET /todos called")

    return service.get_todos()

@router.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo_by_id(todo_id: int, service: TodoService = Depends(get_todo_service)):
    todo = service.get_todo(todo_id)

    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo

@router.post("/todos", response_model=TodoResponse)
def create_todo(todo: Todo, service: TodoService = Depends(get_todo_service)):
    return service.create_todo(
        text=todo.text,
        completed=todo.completed,
    )

@router.put("/todos/{todo_id}", response_model=TodoResponse)
def update(todo_id: int, todo: Todo, service: TodoService = Depends(get_todo_service)):
    updated = service.update_todo(
        todo_id=todo_id,
        text=todo.text,
        completed=todo.completed,
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")

    return updated

@router.delete("/todos/{todo_id}")
def delete(todo_id: int, service: TodoService = Depends(get_todo_service)):
    result = service.delete_todo(todo_id)

    if not result:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {"message": "Todo deleted"}
