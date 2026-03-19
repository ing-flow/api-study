from fastapi import FastAPI

from app.core.logging import setup_logging
from app.routers import todos
from app.middleware.logging_middleware import log_requests
from app.middleware.request_id import request_id_middleware

setup_logging()

app = FastAPI()

app.middleware("http")(log_requests)
app.middleware("http")(request_id_middleware)

app.include_router(todos.router)