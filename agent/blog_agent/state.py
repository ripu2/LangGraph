from typing_extensions import TypedDict


class BlogState(TypedDict, total=False):
    title: str
    outline: str
    content: str
