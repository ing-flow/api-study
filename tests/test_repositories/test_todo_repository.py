from app.repositories.todo_repository import TodoRepository


def test_create_todo(db_session):

    repo = TodoRepository(db_session)

    todo = repo.create("test todo", False)

    assert todo.id is not None
    assert todo.text == "test todo"
    assert todo.completed is False


def test_get_all(db_session):

    repo = TodoRepository(db_session)

    repo.create("todo1", False)
    repo.create("todo2", True)

    todos = repo.get_all()

    assert len(todos) == 2


def test_update_todo(db_session):

    repo = TodoRepository(db_session)

    todo = repo.create("todo1", False)

    updated = repo.update(todo, "updated", True)

    assert updated.text == "updated"
    assert updated.completed is True


def test_delete_todo(db_session):

    repo = TodoRepository(db_session)

    todo = repo.create("todo1", False)

    repo.delete(todo)

    result = repo.get(todo.id)

    assert result is None