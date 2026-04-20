from typing_extensions import TypedDict


class CricketState(TypedDict):
    total_runs: int
    total_balls: int
    total_fours: int
    total_sixes: int
    strike_rate: float
    boundary_percentage: float
    summary: str
