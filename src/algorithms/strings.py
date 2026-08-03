"""String-processing algorithms."""

from collections import Counter


def is_palindrome(text: str) -> bool:
    """Return whether text reads identically backward. Time/space: O(n)."""
    return text == text[::-1]


def caesar_cipher(text: str, shift: int) -> str:
    """Shift ASCII letters while preserving case; leave other characters intact."""
    output: list[str] = []
    for char in text:
        if "a" <= char <= "z":
            output.append(chr((ord(char) - ord("a") + shift) % 26 + ord("a")))
        elif "A" <= char <= "Z":
            output.append(chr((ord(char) - ord("A") + shift) % 26 + ord("A")))
        else:
            output.append(char)
    return "".join(output)


def first_non_repeating_character(text: str) -> int:
    """Return the first unique character's index, or -1. Time/space: O(n)."""
    counts = Counter(text)
    return next((index for index, char in enumerate(text) if counts[char] == 1), -1)


def valid_anagram(left: str, right: str) -> bool:
    """Return whether strings contain the same characters with equal multiplicity."""
    return Counter(left) == Counter(right)


def reverse_words(text: str) -> str:
    """Reverse whitespace-delimited words. Time/space: O(n)."""
    return " ".join(reversed(text.split()))
