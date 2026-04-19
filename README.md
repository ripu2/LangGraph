# Simple AI Agent

A practice project for learning **FastAPI** + **LangGraph** by building AI-powered agents.

## What this project does

Two agents exposed as REST API endpoints:

| Endpoint | What it does |
|---|---|
| `GET /health` | Check if server is running |
| `POST /agent/bmi` | Calculate BMI from weight + height |
| `POST /agent/weather` | Get live weather + GPT-4o-mini advisory report for any location |

## Project Structure

```
simple-ai-agent/
├── agent/
│   ├── bmi_agent/          # BMI calculation LangGraph pipeline
│   │   ├── graph.py        # Node connections (flow)
│   │   ├── nodes.py        # What each step does
│   │   ├── state.py        # Data passed between nodes
│   │   └── tools.py        # Helper functions
│   └── weather_agent/      # Weather fetch + AI report pipeline
│       ├── graph.py
│       ├── nodes.py
│       ├── state.py
│       └── tools.py        # Calls Open-Meteo API
├── app/
│   ├── controllers/        # Business logic, calls agent graphs
│   ├── routes/             # FastAPI route definitions
│   └── schemas/            # Request/response data shapes
└── main.py                 # Entry point
```

## Setup

**Requirements:** Python 3.13+, [uv](https://docs.astral.sh/uv/)

```bash
# Clone and enter project
git clone https://github.com/ripu2/LangGraph.git
cd LangGraph

# Install dependencies
uv sync

# Copy env file and fill in your API keys
cp .env.example .env
```

Edit `.env`:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

> Weather agent uses [Open-Meteo](https://open-meteo.com/) — free, no API key needed.

## Run

```bash
uvicorn main:app --reload
```

Server starts at `http://localhost:8000`

## API Usage

### BMI Calculator

```bash
curl -X POST http://localhost:8000/agent/bmi \
  -H "Content-Type: application/json" \
  -d '{"weight": 70, "height": 1.75}'
```

### Weather Report

```bash
curl -X POST http://localhost:8000/agent/weather \
  -H "Content-Type: application/json" \
  -d '{"latitude": 25.59, "longitude": 85.14}'
```

Returns a GPT-generated weather advisory: what to wear, when to go out, what to avoid — based on live weather data.

## Interactive Docs

FastAPI auto-generates docs at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing with Bruno

[Bruno](https://www.usebruno.com/) collection included. Open Bruno → open folder → select this repo directory.

## How LangGraph works here

Each agent is a **graph** — a series of steps (nodes) connected by edges:

```
BMI Agent:    START → validate_input → calculate_bmi → label_bmi → END
Weather Agent: START → get_weather → parse_weather → END
```

Each node receives the current **state** (shared data), does its work, and returns updated state. LangGraph handles passing data between nodes.

## What I'm learning

- Building REST APIs with FastAPI
- Agent orchestration with LangGraph
- Calling external APIs (Open-Meteo)
- Using LLMs (GPT-4o-mini) inside agent pipelines
- Pydantic for data validation
