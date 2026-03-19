from sqlalchemy.orm import Session
from app.models.todo_model import TodoModel

class TodoRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, text: str, completed: bool):

        todo = TodoModel(
            text=text,
            completed=completed
        )

        self.db.add(todo)
        self.db.commit()
        self.db.refresh(todo)

        return todo

    def get_all(self):

        return self.db.query(TodoModel).all()
    
    def get(self, todo_id: int) -> TodoModel | None:
        return self.db.query(TodoModel).filter(TodoModel.id == todo_id).first()

    def update(self, todo: TodoModel, text: str, completed: bool):

        todo.text = text
        todo.completed = completed

        self.db.commit()
        self.db.refresh(todo)

        return todo

    def delete(self, todo: TodoModel):
        self.db.delete(todo)
        self.db.commit()