from typing import Literal
from typing_extensions import TypedDict


class TweetState(TypedDict):
    topic: str
    tweet: str
    evaluation: Literal["positive", "needs_improvement"]
    feedback: str
    iteration_count: int
    MAX_ITERATIONS: int
