from agent.bmi_agent.state import AgentState
from app.logger import setup_logger

logger = setup_logger(__name__)


def validate_input(state: AgentState) -> AgentState:
    """Validates that weight and height are present and positive."""
    logger.info("[Node: validate_input] Executing")
    logger.debug("[Node: validate_input] Received state: %s", state)

    weight = state["weight_kg"]
    height = state["height_m"]
    logger.debug(
        "[Node: validate_input] Validating weight=%.2f, height=%.2f", weight, height
    )

    if weight <= 0 or height <= 0:
        logger.error(
            "[Node: validate_input] Validation FAILED | weight=%.2f, height=%.2f",
            weight,
            height,
        )
        raise ValueError("Weight and height must be positive numbers")

    logger.info("[Node: validate_input] Validation PASSED")
    return {}


def calculate_bmi(state: AgentState) -> AgentState:
    """Calculates BMI from weight in kilograms and height in meters."""
    logger.info("[Node: calculate_bmi] Executing")
    logger.debug("[Node: calculate_bmi] Received state: %s", state)

    weight = state["weight_kg"]
    height = state["height_m"]
    bmi = round(weight / (height**2), 2)

    logger.info(
        "[Node: calculate_bmi] Computed BMI=%.2f (weight=%.2f / height=%.2f^2)",
        bmi,
        weight,
        height,
    )
    return {"bmi": bmi}
