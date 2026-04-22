from typing import NotRequired
from typing_extensions import TypedDict


class RootFinderState(TypedDict):
    a: int
    b: int
    c: int
    equation: NotRequired[str]
    determinant: NotRequired[float]
    root1: NotRequired[float | complex]
    root2: NotRequired[float | complex]
