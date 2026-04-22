from langgraph.graph import START, StateGraph
from langgraph.graph.state import END
from agent.cricket_agent.nodes import (
    compute_boundary_percentage,
    compute_strike_rate,
    generate_summary,
)
from agent.cricket_agent.state import CricketState
from app.logger import setup_logger


logger = setup_logger(__name__)


def build_graph():
    logger.info("Building cricket agent graph")

    graph = StateGraph(CricketState)
    logger.debug("StateGraph created with CricketState schema")

    graph.add_node("compute_strike_rate", compute_strike_rate)
    logger.debug("Added node: compute_strike_rate")

    graph.add_node("compute_boundary_percentage", compute_boundary_percentage)
    logger.debug("Added node: compute_boundary_percentage")

    graph.add_node("generate_summary", generate_summary)
    logger.debug("Added node: generate_summary")

    graph.add_edge(START, "compute_strike_rate")
    logger.debug("Added edge: START -> compute_strike_rate")
    graph.add_edge(START, "compute_boundary_percentage")
    logger.debug("Added Parallel edge: START -> compute_boundary_percentage")
    graph.add_edge(START, "compute_boundary_percentage")
    logger.debug("Added Parallel edge: START -> compute_boundary_percentage")

    graph.add_edge("compute_strike_rate", "generate_summary")
    logger.debug("Added edge: compute_strike_rate -> generate_summary")
    graph.add_edge("compute_boundary_percentage", "generate_summary")
    logger.debug("Added edge: compute_boundary_percentage -> generate_summary")
    graph.add_edge("generate_summary", END)
    logger.debug("Added edge: generate_summary -> END")

    compiled = graph.compile()
    logger.info(
        "Cricket agent graph compiled | nodes=[compute_strike_rate, compute_boundary_percentage, generate_summary] | flow: START -> compute_strike_rate -> compute_boundary_percentage -> generate_summary -> END"
    )
    return compiled
