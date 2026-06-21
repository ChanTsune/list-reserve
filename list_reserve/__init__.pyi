from typing import Any, TypedDict

def reserve(list: list[Any], capacity: int) -> None:
    """Reserve list capacity.

    Grow the backing storage to hold at least capacity elements. Only ever
    grows: a no-op when capacity already meets or exceeds the request.
    """

def capacity(list: list[Any]) -> int:
    """Return list capacity.

    The number of elements the backing storage can hold before it must grow;
    always greater than or equal to len(list).
    """

def remaining_capacity(list: list[Any]) -> int:
    """Return list remaining capacity.

    Equals capacity(list) - len(list): how many elements can be appended
    before the backing storage must grow.
    """

def allocated_bytes(list: list[Any]) -> int:
    """Return list allocated memory size.

    The size in bytes of the backing item array (capacity times the pointer
    size); excludes the list object header.
    """

def shrink_to_fit(list: list[Any]) -> None:
    """Shrink to fit list capacity.

    Reallocate the backing storage down to the live element count, so that
    capacity(list) equals len(list) afterwards.
    """

class Stats(TypedDict):
    length: int
    capacity: int
    allocated_bytes: int
    remaining_capacity: int
    utilization: float

def stats(list: list[Any]) -> Stats:
    """Return list memory statistics as a dict.

    Utilization is length / capacity (0.0 when capacity is 0); the other keys
    match the same-named functions.
    """
