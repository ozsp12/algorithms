"""Searching algorithms."""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def binary_search(values: Sequence[T], target: T) -> int:
    """Return the index of ``target`` in a sorted sequence, or ``-1``.

    Time: O(log n). Space: O(1). When duplicates exist, any matching index
    may be returned.
    """
    left, right = 0, len(values) - 1
    while left <= right:
        middle = (left + right) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1
