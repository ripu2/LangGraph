from langchain_openai import ChatOpenAI

from agent.weather_agent.state import WeatherState
from agent.weather_agent import tools
from app.logger import setup_logger
from app.model_config import model_config
from app.schemas.weather_schema import WeatherRequest
from agent.prompts.prompts import Prompts
from langchain_core.messages import SystemMessage, HumanMessage


logger = setup_logger(__name__)
_model = ChatOpenAI(**model_config.natural.to_kwargs())


def get_weather(state: WeatherState) -> WeatherState:
    logger.info("[Node: get_weather] Executing")
    request = WeatherRequest(latitude=state["lat"], longitude=state["lon"])
    weather = tools.get_weather(request)
    logger.debug("[Node: get_weather] Received state: %s", state)
    return {"weather": weather}


def parse_weather(state: WeatherState) -> WeatherState:
    logger.info("[Node: parse_weather] Executing")
    weather = state["weather"]
    lat = state["lat"]
    lon = state["lon"]
    messages = [
        SystemMessage(content=Prompts.weather_report), 
        HumanMessage(content=f"The weather data is: {weather}. Also providing the latitude and longitude of the location. so that you can fetch location and in the response use it per your need The location is: {lat}, {lon}"),
    ]
    response = _model.invoke(messages)
    weather_report = response.content
    logger.debug("[Node: parse_weather] Weather report: %s", weather_report)
    return {"weather_report": weather_report}
