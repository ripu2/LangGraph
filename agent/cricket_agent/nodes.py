from agent.cricket_agent.state import CricketState
from app.logger import setup_logger

logger = setup_logger(__name__)


def compute_strike_rate(state: CricketState) -> CricketState:
    logger.info("[Node: compute_strike_rate] Executing")
    total_runs = state["total_runs"]
    total_balls = state["total_balls"]
    strike_rate = round((total_runs / total_balls) * 100, 2)
    logger.debug("[Node: compute_strike_rate] Received state: %s", state)
    return {"strike_rate": strike_rate}


def compute_boundary_percentage(state: CricketState) -> CricketState:
    logger.info("[Node: compute_boundary_percentage] Executing")
    total_fours = state["total_fours"]
    total_sixes = state["total_sixes"]
    total_runs = state["total_runs"]
    boundary_percentage = round(((total_fours * 4 + total_sixes * 6) / total_runs) * 100, 2)
    logger.debug("[Node: compute_boundary_percentage] Received state: %s", state)
    return {"boundary_percentage": boundary_percentage}


def generate_summary(state: CricketState) -> CricketState:
    logger.info("[Node: generate_summary] Executing")
    total_runs = state["total_runs"]
    total_balls = state["total_balls"]
    total_fours = state["total_fours"]
    total_sixes = state["total_sixes"]
    strike_rate = state["strike_rate"]
    boundary_percentage = state["boundary_percentage"]
    summary = f"The Batsman scored {total_runs} runs in {total_balls} balls with {total_fours} fours and {total_sixes} sixes with a strike rate of {strike_rate} and a boundary percentage of {boundary_percentage}"
    logger.debug("[Node: generate_summary] Received state: %s", state)
    return {"summary": summary}
