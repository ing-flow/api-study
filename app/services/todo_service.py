from app.repositories.todo_repository import TodoRepository
from app.core.logger import get_app_logger

logger = get_app_logger(__name__)

class TodoService:

    def __init__(self, repo: TodoRepository):
        self.repo = repo

    def get_todo(self, todo_id: int):
        return self.repo.get(todo_id)

    def get_todos(self):
        return self.repo.get_all()

    def create_todo(self, text: str, completed: bool):
        try:
            logger.info(
                "creating todo",
                extra={"text": text}
            )

            todo = self.repo.create(text, completed)
            
            logger.info(
                "todo created",
                extra={"todo_id": todo.id}
            )

            return todo
        except Exception as e:

            logger.error(f"todo create failed: {e}")

            raise

    def update_todo(self, todo_id: int, text: str, completed: bool):

        todo = self.repo.get(todo_id)

        if not todo:
            return None

        return self.repo.update(todo, text, completed)

    def delete_todo(self, todo_id: int):

        todo = self.repo.get(todo_id)

        if not todo:
            return False

        self.repo.delete(todo)

        return True










