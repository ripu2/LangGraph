from langgraph.graph import StateGraph, START, END
from agent.bmi_agent.state import AgentState
from agent.bmi_agent.nodes import validate_input, calculate_bmi
from app.logger import setup_logger

logger = setup_logger(__name__)


def build_graph():
    logger.info("Building agent graph")

    graph = StateGraph(AgentState)
    logger.debug("StateGraph created with AgentState schema")

    graph.add_node("validate_input", validate_input)
    logger.debug("Added node: validate_input")

    graph.add_node("calculate_bmi", calculate_bmi)
    logger.debug("Added node: calculate_bmi")

    graph.add_edge(START, "validate_input")
    logger.debug("Added edge: START -> validate_input")

    graph.add_edge("validate_input", "calculate_bmi")
    logger.debug("Added edge: validate_input -> calculate_bmi")

    graph.add_edge("calculate_bmi", END)
    logger.debug("Added edge: calculate_bmi -> END")

    compiled = graph.compile()
    logger.info(
        "Agent graph compiled | nodes=[validate_input, calculate_bmi] | "
        "flow: START -> validate_input -> calculate_bmi -> END"
    )
    return compiled
