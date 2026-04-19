import time
from app.logger import setup_logger
from app.schemas.weather_schema import WeatherRequest
from agent.weather_agent.graph import build_graph

logger = setup_logger(__name__)


class WeatherController:
    def __init__(self):
        self.graph = build_graph()
        logger.debug("WeatherController initialized with compiled graph")

    def get_weather(self, request: WeatherRequest):
        input_state = {"lat": request.latitude, "lon": request.longitude}
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
            return result["weather_report"]
        except Exception as exc:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(
                "Agent graph failed | %.2fms | error=%s",
                duration_ms,
                str(exc),
                exc_info=True,
            )
            raise
