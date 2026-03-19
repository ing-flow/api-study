from app.services.todo_service import TodoService
from app.models.todo_model import TodoModel


class FakeTodoRepository:

    def create(self, text, completed):
        return TodoModel(
            id=1,
            text=text,
            completed=completed
        )

    def get(self, todo_id):
        if todo_id == 1:
            return TodoModel(id=1, text="test", completed=False)
        return None

    def get_all(self):
        return [
            TodoModel(id=1, text="test1", completed=False),
            TodoModel(id=2, text="test2", completed=True),
        ]

def test_create_todo():

    fake_repo = FakeTodoRepository()

    service = TodoService(fake_repo)

    todo = service.create_todo(
        text="learn fastapi",
        completed=False
    )

    assert todo.text == "learn fastapi"
    assert todo.completed is False

def test_list_todos():

    fake_repo = FakeTodoRepository()

    service = TodoService(fake_repo)

    todos = service.get_todos()

    assert len(todos) == 2