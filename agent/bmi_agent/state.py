from typing import TypedDict


class AgentState(TypedDict, total=False):
    weight_kg: float
    height_m: float
    bmi: float
