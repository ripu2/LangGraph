from langgraph.graph import END, StateGraph
from langgraph.graph.state import START
from agent.blog_agent.nodes import generate_content, generate_outline
from agent.blog_agent.state import BlogState
from app.logger import setup_logger

logger = setup_logger(__name__)


def build_graph():
    logger.info("Building blog agent graph")

    graph = StateGraph(BlogState)
    graph.add_node("generate_outline", generate_outline)
    logger.debug("Added node: generate_outline")
    graph.add_node("generate_content", generate_content)
    logger.debug("Added node: generate_content")

    graph.add_edge(START, "generate_outline")
    logger.debug("Added edge: START -> generate_outline")
    graph.add_edge("generate_outline", "generate_content")
    logger.debug("Added edge: generate_outline -> generate_content")
    graph.add_edge("generate_content", END)
    logger.debug("Added edge: generate_content -> END")

    compiled = graph.compile()
    logger.info(
        "Blog agent graph compiled | nodes=[generate_outline, generate_content] | flow: START -> generate_outline -> generate_content -> END"
    )
    return compiled
