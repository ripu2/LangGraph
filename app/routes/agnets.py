from fastapi import APIRouter

from app.controllers.blog_controller import BlogController
from app.controllers.bmi_controller import BMIController
from app.controllers.cricket_controlle import CricketController
from app.controllers.weather_controller import WeatherController
from app.logger import setup_logger
from app.schemas.blog_schema import BlogRequest
from app.schemas.bmi_schema import CalculateBMIRequest
from app.schemas.cricket_schema import CricketRequest
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


@router.post("/cricket")
def compute_strike_rate(request: CricketRequest):
    logger.info(
        "Cricket endpoint called | total_runs=%d, total_balls=%d, total_fours=%d, total_sixes=%d",
        request.total_runs,
        request.total_balls,
        request.total_fours,
        request.total_sixes,
    )
    try:
        result = CricketController().compute_strike_rate(request)
        logger.info("Cricket endpoint completed successfully | result=%s", result)
        return result
    except Exception as exc:
        logger.error("Cricket endpoint failed | error=%s", str(exc), exc_info=True)
        raise
