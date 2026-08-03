"""Algorithms for arrays and numeric sequences."""

from collections.abc import Sequence


def two_number_sum(values: Sequence[int], target: int) -> tuple[int, int] | None:
    """Return two distinct values summing to target. Time/space: O(n)."""
    seen: set[int] = set()
    for value in values:
        complement = target - value
        if complement in seen:
            return complement, value
        seen.add(value)
    return None


def sorted_squared_array(values: Sequence[int | float]) -> list[int | float]:
    """Square a sorted sequence and retain sorted order. Time/space: O(n)."""
    result = [0] * len(values)
    left, right = 0, len(values) - 1
    for output in range(len(values) - 1, -1, -1):
        if abs(values[left]) > abs(values[right]):
            result[output] = values[left] ** 2; left += 1
        else:
            result[output] = values[right] ** 2; right -= 1
    return result


def running_sum(values: Sequence[int | float]) -> list[int | float]:
    """Return prefix sums. Time: O(n); auxiliary space: O(1)."""
    result: list[int | float] = []
    total: int | float = 0
    for value in values:
        total += value
        result.append(total)
    return result


def three_number_sum(values: Sequence[int], target: int) -> list[tuple[int, int, int]]:
    """Return unique sorted triplets summing to target. Time: O(n²)."""
    ordered = sorted(values)
    triplets: set[tuple[int, int, int]] = set()
    for index in range(len(ordered) - 2):
        left, right = index + 1, len(ordered) - 1
        while left < right:
            total = ordered[index] + ordered[left] + ordered[right]
            if total == target:
                triplets.add((ordered[index], ordered[left], ordered[right]))
                left += 1; right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    return sorted(triplets)


def kadane(values: Sequence[int | float]) -> int | float:
    """Return the maximum contiguous-subarray sum. Time: O(n); space: O(1)."""
    if not values:
        raise ValueError("kadane requires at least one value")
    best_ending = best = values[0]
    for value in values[1:]:
        best_ending = max(value, best_ending + value)
        best = max(best, best_ending)
    return best
