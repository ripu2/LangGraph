from pydantic import BaseModel


class RootRequest(BaseModel):
    a: int
    b: int
    c: int


class RootResponse(BaseModel):
    root1: float | str
    root2: float | str
