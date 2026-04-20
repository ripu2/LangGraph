from pydantic import BaseModel


class BlogRequest(BaseModel):
    title: str


class BlogResponse(BaseModel):
    outline: str
    content: str
