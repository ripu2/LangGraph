from typing import TypedDict

from app.schemas.weather_schema import WeatherResponse


class WeatherState(TypedDict, total=False):
    lat: float
    lon: float
    weather: WeatherResponse
    weather_report: str
