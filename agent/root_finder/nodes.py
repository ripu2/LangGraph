import math
from agent.root_finder.state import RootFinderState
from app.logger import setup_logger

logger = setup_logger(__name__)


def generate_equation(state: RootFinderState) -> RootFinderState:
    a = state["a"]
    b = state["b"]
    c = state["c"]
    logger.info("[Node: generate_equation] Executing")
    logger.debug("[Node: generate_equation] Received state: %s", state)
    equation = f"{a}x^2 + {b}x + {c} = 0"
    logger.debug("[Node: generate_equation] Equation: %s", equation)
    return {"equation": equation}


def calculate_determinant(state: RootFinderState) -> RootFinderState:
    a = state["a"]
    b = state["b"]
    c = state["c"]
    logger.info("[Node: calculate_determinant] Executing")
    logger.debug("[Node: calculate_determinant] Received state: %s", state)
    determinant = b**2 - 4 * a * c
    logger.debug("[Node: calculate_determinant] Determinant: %s", determinant)
    return {"determinant": determinant}


def calculate_roots_if_real_and_distinct(state: RootFinderState) -> RootFinderState:
    determinant = state["determinant"]
    a = state["a"]
    b = state["b"]
    root1 = round(((-b + math.sqrt(determinant)) / (2 * a)), 2)
    root2 = round(((-b - math.sqrt(determinant)) / (2 * a)), 2)
    logger.debug(
        "[Node: calculate_roots_if_real_and_distinct] Roots: %s, %s", root1, root2
    )
    return {"root1": root1, "root2": root2}


def calculate_roots_if_real_and_equal(state: RootFinderState) -> RootFinderState:
    a = state["a"]
    b = state["b"]
    root = round((-b / (2 * a)), 2)
    logger.debug("[Node: calculate_roots_if_real_and_equal] Root: %s", root)
    return {"root1": root, "root2": root}


def calculate_roots_if_complex(state: RootFinderState) -> RootFinderState:
    determinant = state["determinant"]
    a = state["a"]
    b = state["b"]
    root1 = complex(
        round((-b / (2 * a)), 2), round((math.sqrt(-determinant) / (2 * a)), 2)
    )
    root2 = complex(
        round((-b / (2 * a)), 2), round((-math.sqrt(-determinant) / (2 * a)), 2)
    )
    logger.debug("[Node: calculate_roots_if_complex] Roots: %s, %s", root1, root2)
    return {"root1": root1, "root2": root2}


def route_by_determinant(state: RootFinderState) -> str:
    determinant = state["determinant"]
    if determinant > 0:
        return "calculate_roots_if_real_and_distinct"
    if determinant == 0:
        return "calculate_roots_if_real_and_equal"
    return "calculate_roots_if_complex"
