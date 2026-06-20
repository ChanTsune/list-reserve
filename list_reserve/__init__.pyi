from typing import Any, TypedDict

def reserve(list: list[Any], capacity: int) -> None:
    """Reserve list capacity."""

def capacity(list: list[Any]) -> int:
    """Return list capacity."""

def allocated_bytes(list: list[Any]) -> int:
    """Return list allocated memory size."""

def shrink_to_fit(list: list[Any]) -> None:
    """Shrink to fit list capacity."""

class Stats(TypedDict):
    length: int
    capacity: int
    allocated_bytes: int
    overhead: int
    utilization: float

def stats(list: list[Any]) -> Stats:
    """Return list memory statistics as a dict."""
