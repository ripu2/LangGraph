from langgraph.graph import END, START, StateGraph
from agent.weather_agent.nodes import get_weather, parse_weather
from agent.weather_agent.state import WeatherState
from app.logger import setup_logger

logger = setup_logger(__name__)


def build_graph():
    logger.info("Building agent graph")

    graph = StateGraph(WeatherState)
    logger.debug("StateGraph created with WeatherState schema")

    graph.add_node("get_weather", get_weather)
    logger.debug("Added node: get_weather")

    graph.add_node("parse_weather", parse_weather)
    logger.debug("Added node: parse_weather")

    graph.add_edge(START, "get_weather")
    logger.debug("Added edge: START -> get_weather")

    graph.add_edge("get_weather", "parse_weather")
    logger.debug("Added edge: get_weather -> parse_weather")

    graph.add_edge("parse_weather", END)
    logger.debug("Added edge: parse_weather -> END")

    compiled = graph.compile()
    logger.info(
        "Agent graph compiled | nodes=[get_weather, parse_weather] | flow: START -> get_weather -> parse_weather -> END"
    )
    return compiled
