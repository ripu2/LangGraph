from langgraph.graph import StateGraph
from agent.root_finder.state import RootFinderState
from agent.root_finder.nodes import (
    calculate_roots_if_complex,
    calculate_roots_if_real_and_distinct,
    calculate_roots_if_real_and_equal,
    generate_equation,
    calculate_determinant,
    route_by_determinant,
)
from app.logger import setup_logger

logger = setup_logger(__name__)

def build_graph():
    logger.info("[Graph: build_graph] Building graph")
    graph = StateGraph(RootFinderState)
    graph.add_node("generate_equation", generate_equation)
    logger.debug("[Graph: build_graph] Added node: generate_equation")
    graph.add_node("calculate_determinant", calculate_determinant)

    graph.add_node(
        "calculate_roots_if_real_and_distinct", calculate_roots_if_real_and_distinct
    )
    logger.debug("[Graph: build_graph] Added node: calculate_determinant")

    graph.add_node(
        "calculate_roots_if_real_and_equal", calculate_roots_if_real_and_equal
    )
    logger.debug("[Graph: build_graph] Added node: calculate_roots_if_real_and_equal")

    graph.add_node("calculate_roots_if_complex", calculate_roots_if_complex)
    logger.debug("[Graph: build_graph] Added node: calculate_roots_if_complex")

    graph.set_entry_point("generate_equation")
    logger.debug("[Graph: build_graph] Set entry point: generate_equation")
    graph.add_edge("generate_equation", "calculate_determinant")
    logger.debug(
        "[Graph: build_graph] Added edge: generate_equation -> calculate_determinant"
    )
    graph.add_conditional_edges("calculate_determinant", route_by_determinant)

    graph.set_finish_point("calculate_roots_if_real_and_distinct")
    logger.debug(
        "[Graph: build_graph] Set finish point: calculate_roots_if_real_and_distinct"
    )

    graph.set_finish_point("calculate_roots_if_real_and_equal")
    logger.debug(
        "[Graph: build_graph] Set finish point: calculate_roots_if_real_and_equal"
    )

    graph.set_finish_point("calculate_roots_if_complex")
    logger.debug("[Graph: build_graph] Set finish point: calculate_roots_if_complex")

    compiled = graph.compile()
    logger.info("[Graph: build_graph] Graph compiled")
    return compiled
