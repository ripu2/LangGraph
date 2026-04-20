from pydantic.main import BaseModel


class CricketRequest(BaseModel):
    total_runs: int
    total_balls: int
    total_fours: int
    total_sixes: int


class CricketResponse(BaseModel):
    strike_rate: float
    boundary_percentage: float
    summary: str
