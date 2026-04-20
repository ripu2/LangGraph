import time
from agent.blog_agent.graph import build_graph
from app.logger import setup_logger
from app.schemas.blog_schema import BlogRequest


logger = setup_logger(__name__)

_blog_graph = build_graph()


class BlogController:
    def __init__(self):
        self.graph = _blog_graph
        logger.debug("BlogController initialized with compiled graph")

    def generate_blog(self, request: BlogRequest):
        input_state = {"title": request.title}
        logger.info("Invoking agent graph | input_state=%s", input_state)
        start_time = time.time()
        try:
            result = self.graph.invoke(input_state)
            duration_ms = (time.time() - start_time) * 1000
            logger.info(
                "Agent graph completed | output_state=%s | %.2fms",
                result,
                duration_ms,
            )
            return result
        except Exception as exc:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(
                "Agent graph failed | %.2fms | error=%s",
                duration_ms,
                str(exc),
                exc_info=True,
            )
            raise
