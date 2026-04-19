from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from agent.weather_agent.state import WeatherState
from agent.weather_agent import tools
from app.logger import setup_logger
from app.model_config import model_config
from app.schemas.weather_schema import WeatherRequest


logger = setup_logger(__name__)

load_dotenv()


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
    prompt = f"You are an expert weather analyst. Your task is to analyze the weather data and provide a detailed report about the weather and also tell the locals about how to plan their day in structured way like what to wear, what to carry please take a note that the weather report should start with the name of city which you will fetch from latitude and longitude provided in the prompt, what to avoid, etc at which time to avoid going out and what to do if you are out. The weather data is: {weather}. Also providing the latitude and longitude of the location. so that you can fetch location and in the response use it per your need The location is: {lat}, {lon}"
    logger.info(
        "Sending prompt to GPT for weather report | profile=natural | model=%s | temperature=%s",
        model_config.natural.model,
        model_config.natural.temperature,
    )
    model = ChatOpenAI(**model_config.natural.to_kwargs())
    response = model.invoke(prompt)
    weather_report = response.content
    state["weather_report"] = weather_report
    logger.debug("[Node: parse_weather] Weather report: %s", weather_report)
    return state
