from typing import Literal
from pydantic import BaseModel, Field


class TweetRequest(BaseModel):
    topic: str


class TweetResponse(BaseModel):
    evaluation: Literal["positive", "needs_improvement"]
    feedback: str = Field(..., description="Feedback on the tweet")
