from fastapi import APIRouter

from app.controllers.bmi_controller import BMIController
from app.logger import setup_logger
from app.schemas.bmi_schema import CalculateBMIRequest

logger = setup_logger(__name__)

router = APIRouter(prefix="/agent", tags=["agent"])


@router.post("/bmi")
def calculate_bmi(request: CalculateBMIRequest):
    logger.info(
        "BMI endpoint called | weight=%.2f kg, height=%.2f m",
        request.weight,
        request.height,
    )
    try:
        result = BMIController().calculate_bmi(request)
        logger.info("BMI endpoint completed successfully | result=%s", result)
        return result
    except Exception as exc:
        logger.error("BMI endpoint failed | error=%s", str(exc), exc_info=True)
        raise
