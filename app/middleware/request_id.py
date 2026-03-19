import uuid
import contextvars
from fastapi import Request

request_id_var = contextvars.ContextVar("request_id", default="-")

async def request_id_middleware(request: Request, call_next):

    request_id = str(uuid.uuid4())[:8]

    request_id_var.set(request_id)

    response = await call_next(request)

    response.headers["X-Request-ID"] = request_id

    return response