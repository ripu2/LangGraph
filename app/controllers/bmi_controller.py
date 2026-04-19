import time

from agent.bmi_agent.graph import build_graph
from app.logger import setup_logger
from app.schemas.bmi_schema import CalculateBMIRequest

logger = setup_logger(__name__)


class BMIController:
    def __init__(self):
        logger.debug("Initializing BMIController")
        self.graph = build_graph()
        logger.debug("BMIController initialized with compiled graph")

    def calculate_bmi(self, request: CalculateBMIRequest):
        input_state = {"weight_kg": request.weight, "height_m": request.height}
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
