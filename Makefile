up:
	docker compose up --build

down:
	docker compose down

logs:
	docker compose logs -f

ps:
	docker compose ps

test:
	pytest

migrate:
	docker compose exec app alembic upgrade head

revision:
	docker compose exec app alembic revision --autogenerate -m "migration"

lint:
	ruff check .

format:
	ruff format .