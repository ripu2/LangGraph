from pydantic import BaseModel, Field


class CalculateBMIRequest(BaseModel):
    weight: float = Field(gt=0, description="Weight in kilograms")
    height: float = Field(gt=0, description="Height in meters")
