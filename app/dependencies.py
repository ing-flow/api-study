from fastapi import Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.repositories.todo_repository import TodoRepository
from app.services.todo_service import TodoService


def get_todo_repository(
    db: Session = Depends(get_db),
) -> TodoRepository:
    return TodoRepository(db)


def get_todo_service(
    repo: TodoRepository = Depends(get_todo_repository),
) -> TodoService:
    return TodoService(repo)