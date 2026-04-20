from fastapi import APIRouter

from app.controllers.blog_controller import BlogController
from app.controllers.bmi_controller import BMIController
from app.controllers.weather_controller import WeatherController
from app.logger import setup_logger
from app.schemas.blog_schema import BlogRequest
from app.schemas.bmi_schema import CalculateBMIRequest
from app.schemas.weather_schema import WeatherRequest

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


@router.post("/weather")
def get_weather(request: WeatherRequest):
    logger.info(
        "Weather endpoint called | latitude=%.2f, longitude=%.2f",
        request.latitude,
        request.longitude,
    )
    try:
        result = WeatherController().get_weather(request)
        logger.info("Weather endpoint completed successfully | result=%s", result)
        return result
    except Exception as exc:
        logger.error("Weather endpoint failed | error=%s", str(exc), exc_info=True)
        raise


@router.post("/blog")
def generate_blog(request: BlogRequest):
    logger.info("Blog endpoint called | title=%s", request.title)
    try:
        result = BlogController().generate_blog(request)
        logger.info("Blog endpoint completed successfully | result=%s", result)
        return result
    except Exception as exc:
        logger.error("Blog endpoint failed | error=%s", str(exc), exc_info=True)
        raise
