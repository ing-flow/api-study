import time
from fastapi import Request
from app.core.logger import get_access_logger

logger = get_access_logger()

async def log_requests(request: Request, call_next):

    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000

    logger.info(
        "request",
        extra={
            "client": request.client.host,
            "method": request.method,
            "path": request.url.path,
            "status": response.status_code,
            "latency_ms": round(process_time, 2),
        }
    )

    return response