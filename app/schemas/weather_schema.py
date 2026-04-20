from __future__ import annotations

from pydantic import BaseModel, Field


class WeatherRequest(BaseModel):
    latitude: float = Field(
        ..., ge=-90, le=90, description="Latitude (-90 to 90)", examples=[35.6895]
    )
    longitude: float = Field(
        ..., ge=-180, le=180, description="Longitude (-180 to 180)", examples=[139.6917]
    )


class WeatherResponse(BaseModel):
    # --- location ---
    latitude: float = Field(..., description="Latitude used for the lookup")
    longitude: float = Field(..., description="Longitude used for the lookup")
    timezone: str = Field(
        ..., description="Timezone of the coordinates (e.g. 'Asia/Tokyo')"
    )

    # --- current conditions ---
    temperature: float = Field(..., description="Current air temperature at 2 m (°C)")
    feels_like: float = Field(
        ..., description="Apparent (feels-like) temperature at 2 m (°C)"
    )
    humidity: int = Field(..., description="Relative humidity at 2 m (%)")
    wind_speed: float = Field(..., description="Current wind speed at 10 m (km/h)")
    precipitation: float = Field(..., description="Current precipitation (mm)")
    condition: str = Field(..., description="Human-readable weather condition")
    weather_code: int = Field(..., description="WMO weather interpretation code")

    # --- today's forecast ---
    temperature_max: float = Field(..., description="Today's maximum temperature (°C)")
    temperature_min: float = Field(..., description="Today's minimum temperature (°C)")
    precipitation_probability: int = Field(
        ..., description="Today's max precipitation probability (%)"
    )
    precipitation_sum: float = Field(
        ..., description="Today's total precipitation (mm)"
    )
    rain_sum: float = Field(..., description="Today's total rainfall (mm)")
    snowfall_sum: float = Field(..., description="Today's total snowfall (cm)")
    wind_speed_max: float = Field(..., description="Today's maximum wind speed (km/h)")
    wind_gusts_max: float = Field(..., description="Today's maximum wind gusts (km/h)")
    severe: bool = Field(
        ...,
        description="True when today's WMO code indicates showers, thunderstorm, or hail (code ≥ 80)",
    )
