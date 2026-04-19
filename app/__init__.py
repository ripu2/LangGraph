import time
import uuid

from fastapi import FastAPI, Request
from app.logger import setup_logger
from app.routes import bmi, health

logger = setup_logger(__name__)


def create_app() -> FastAPI:
    logger.info("Initializing FastAPI application")
    app = FastAPI(title="Simple AI Agent")

    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        request_id = str(uuid.uuid4())[:8]
        logger.info(
            "[req:%s] --> %s %s",
            request_id,
            request.method,
            request.url.path,
        )
        logger.debug(
            "[req:%s] Headers: %s",
            request_id,
            dict(request.headers),
        )

        start_time = time.time()
        try:
            response = await call_next(request)
            duration_ms = (time.time() - start_time) * 1000
            logger.info(
                "[req:%s] <-- %s %s | status=%d | %.2fms",
                request_id,
                request.method,
                request.url.path,
                response.status_code,
                duration_ms,
            )
            return response
        except Exception as exc:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(
                "[req:%s] <-- %s %s | FAILED | %.2fms | error=%s",
                request_id,
                request.method,
                request.url.path,
                duration_ms,
                str(exc),
            )
            raise

    app.include_router(health.router)
    logger.debug("Registered health routes")
    app.include_router(bmi.router)
    logger.debug("Registered BMI agent routes")

    logger.info("FastAPI application initialized successfully")
    return app
