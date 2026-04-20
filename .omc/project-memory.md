# Project Memory

## Working Preferences
- Avoid repeated full-repo scans.
- Start from this file for context, then read only the files directly related to the task.
- Prefer small, targeted edits.

## Repo Overview
- Runtime: Python 3.13
- App framework: FastAPI
- Graph/orchestration: LangGraph
- LLM client: `langchain-openai`
- Entry point: `main.py`
- App factory: `app/__init__.py:create_app`

## Main Structure
- `main.py`: creates the FastAPI app and logs startup.
- `app/__init__.py`: app factory, request logging middleware, route registration.
- `app/routes/agnets.py`: agent endpoints for BMI and weather.
- `app/routes/health.py`: health endpoint.
- `app/controllers/`: controllers that build and invoke LangGraph graphs.
- `agent/bmi_agent/`: BMI state, nodes, and graph.
- `agent/weather_agent/`: weather state, nodes, graph, and Open-Meteo fetch logic.
- `app/schemas/`: Pydantic request/response models.

## Current Endpoints
- `GET /health`
- `POST /agent/bmi`
- `POST /agent/weather`

## Local Run Command
- `make run`
- Expands to: `uv run uvicorn main:app --reload`

## Implementation Notes
- BMI flow: `validate_input -> calculate_bmi -> label_bmi`
- Weather flow: fetches structured weather from Open-Meteo, then asks the LLM to turn it into a natural-language report.
- `WeatherController.get_weather()` returns only `result["weather_report"]`, not the full graph state.
- Logging is intentionally verbose across app startup, middleware, routes, controllers, and graph nodes.

## Known Naming Quirks
- Route file is named `app/routes/agnets.py`.

## Review Notes To Revisit
- `.env.example` lists API keys that do not all appear to be used by the current code.
- `agent/weather_agent/nodes.py` builds a long prompt inline and relies on the model to infer city name from lat/lon.
- `agent/weather_agent/tools.py` uses direct `httpx.get(...)` instead of a shared client.
