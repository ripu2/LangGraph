from agent.cricket_agent.graph import build_graph
from app.logger import setup_logger
from app.schemas.cricket_schema import CricketRequest
import time

logger = setup_logger(__name__)


class CricketController:
    def __init__(self):
        self.graph = build_graph()
        logger.debug("CricketController initialized with compiled graph")

    def compute_strike_rate(self, request: CricketRequest):
        input_state = {
            "total_runs": request.total_runs,
            "total_balls": request.total_balls,
            "total_fours": request.total_fours,
            "total_sixes": request.total_sixes,
        }
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
