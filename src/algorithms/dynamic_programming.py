"""Dynamic-programming reference implementations."""

from collections.abc import Sequence


def fibonacci(n: int) -> int:
    """Return F(n), with F(0)=0 and F(1)=1. Time: O(n); space: O(1)."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous


def number_of_ways_to_make_change(amount: int, coins: Sequence[int]) -> int:
    """Count unordered combinations producing amount. Time: O(amount × coins)."""
    if amount < 0 or any(coin <= 0 for coin in coins):
        raise ValueError("amount must be nonnegative and coins positive")
    ways = [0] * (amount + 1); ways[0] = 1
    for coin in coins:
        for subtotal in range(coin, amount + 1):
            ways[subtotal] += ways[subtotal - coin]
    return ways[amount]


def minimum_coins(amount: int, coins: Sequence[int]) -> int:
    """Return the fewest coins forming amount, or -1. Time: O(amount × coins)."""
    if amount < 0 or any(coin <= 0 for coin in coins):
        raise ValueError("amount must be nonnegative and coins positive")
    counts = [amount + 1] * (amount + 1); counts[0] = 0
    for subtotal in range(1, amount + 1):
        for coin in coins:
            if coin <= subtotal:
                counts[subtotal] = min(counts[subtotal], counts[subtotal - coin] + 1)
    return -1 if counts[amount] > amount else counts[amount]


def levenshtein_distance(left: str, right: str) -> int:
    """Return edit distance under unit insert/delete/substitute costs. O(mn) time."""
    previous = list(range(len(right) + 1))
    for i, left_char in enumerate(left, 1):
        current = [i]
        for j, right_char in enumerate(right, 1):
            current.append(min(current[-1] + 1, previous[j] + 1,
                               previous[j - 1] + (left_char != right_char)))
        previous = current
    return previous[-1]
