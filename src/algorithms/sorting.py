"""Comparison-based sorting algorithms that leave their inputs unchanged."""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def bubble_sort(values: Sequence[T]) -> list[T]:
    """Return values in ascending order. Time: O(n²); space: O(n)."""
    result = list(values)
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break
    return result


def insertion_sort(values: Sequence[T]) -> list[T]:
    """Return values in ascending order. Time: O(n²); space: O(n)."""
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index
        while position > 0 and result[position - 1] > current:
            result[position] = result[position - 1]
            position -= 1
        result[position] = current
    return result


def selection_sort(values: Sequence[T]) -> list[T]:
    """Return values in ascending order. Time: O(n²); space: O(n)."""
    result = list(values)
    for start in range(len(result)):
        minimum = min(range(start, len(result)), key=result.__getitem__)
        result[start], result[minimum] = result[minimum], result[start]
    return result


def merge_sort(values: Sequence[T]) -> list[T]:
    """Return values in ascending order. Time: O(n log n); space: O(n)."""
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left, right = merge_sort(values[:middle]), merge_sort(values[middle:])
    merged: list[T] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    return merged + left[i:] + right[j:]


def quick_sort(values: Sequence[T]) -> list[T]:
    """Return values in ascending order. Average O(n log n), worst O(n²)."""
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [value for value in values if value < pivot]
    equal = [value for value in values if value == pivot]
    higher = [value for value in values if value > pivot]
    return quick_sort(lower) + equal + quick_sort(higher)
