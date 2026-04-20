from __future__ import annotations

import httpx

from app.logger import setup_logger
from app.schemas.weather_schema import WeatherRequest, WeatherResponse

logger = setup_logger(__name__)

_FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

_WMO_DESCRIPTIONS: dict[int, str] = {
    0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Depositing rime fog",
    51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
    71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow", 77: "Snow grains",
    80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
    85: "Slight snow showers", 86: "Heavy snow showers",
    95: "Thunderstorm", 96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail",
}


def get_weather(request: WeatherRequest) -> WeatherResponse:
    logger.info("Fetching weather for lat=%.2f, lon=%.2f", request.latitude, request.longitude)

    params = {
        "latitude": request.latitude,
        "longitude": request.longitude,
        "current": "temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m,precipitation,weather_code",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,rain_sum,snowfall_sum,wind_speed_10m_max,wind_gusts_10m_max",
        "wind_speed_unit": "kmh",
        "forecast_days": 1,
        "timezone": "auto",
    }

    response = httpx.get(_FORECAST_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    cur = data["current"]
    daily = data["daily"]
    weather_code = int(cur["weather_code"])

    return WeatherResponse(
        latitude=request.latitude,
        longitude=request.longitude,
        timezone=data.get("timezone", "UTC"),
        temperature=round(cur["temperature_2m"], 1),
        feels_like=round(cur["apparent_temperature"], 1),
        humidity=int(cur["relative_humidity_2m"]),
        wind_speed=round(cur["wind_speed_10m"], 1),
        precipitation=round(cur["precipitation"], 2),
        weather_code=weather_code,
        condition=_WMO_DESCRIPTIONS.get(weather_code, "Unknown"),
        temperature_max=round(daily["temperature_2m_max"][0], 1),
        temperature_min=round(daily["temperature_2m_min"][0], 1),
        precipitation_probability=int(daily["precipitation_probability_max"][0]),
        precipitation_sum=round(daily["precipitation_sum"][0], 2),
        rain_sum=round(daily["rain_sum"][0], 2),
        snowfall_sum=round(daily["snowfall_sum"][0], 2),
        wind_speed_max=round(daily["wind_speed_10m_max"][0], 1),
        wind_gusts_max=round(daily["wind_gusts_10m_max"][0], 1),
        severe=weather_code >= 80,
    )
