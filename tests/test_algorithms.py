import pytest

from algorithms import (
    binary_search, breadth_first_search, bubble_sort, caesar_cipher,
    depth_first_search, dijkstra, fibonacci, first_non_repeating_character,
    insertion_sort, is_palindrome, kadane, levenshtein_distance, merge_sort,
    minimum_coins, number_of_ways_to_make_change, quick_sort, reverse_words,
    running_sum, selection_sort, sorted_squared_array, three_number_sum,
    two_number_sum, valid_anagram,
)


@pytest.mark.parametrize("algorithm", [bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort])
def test_sorting_algorithms(algorithm):
    values = [5, -1, 3, 3, 0]
    assert algorithm(values) == [-1, 0, 3, 3, 5]
    assert values == [5, -1, 3, 3, 0]


def test_search_and_arrays():
    assert binary_search([1, 3, 5, 8], 5) == 2
    assert binary_search([], 5) == -1
    assert set(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10)) == {-1, 11}
    assert sorted_squared_array([-7, -3, 1, 9]) == [1, 9, 49, 81]
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0) == [(-8, 2, 6), (-8, 3, 5), (-6, 1, 5)]
    assert kadane([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]) == 19
    with pytest.raises(ValueError):
        kadane([])


def test_strings():
    assert is_palindrome("level")
    assert caesar_cipher("Zebra-123", 2) == "Bgdtc-123"
    assert first_non_repeating_character("abcdcaf") == 1
    assert valid_anagram("listen", "silent")
    assert reverse_words("  algorithms   are useful ") == "useful are algorithms"


def test_graphs():
    graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
    assert breadth_first_search(graph, "A") == ["A", "B", "C", "D"]
    assert depth_first_search(graph, "A") == ["A", "B", "D", "C"]
    weighted = {"A": {"B": 4, "C": 1}, "C": {"B": 2}, "B": {}}
    assert dijkstra(weighted, "A") == {"A": 0.0, "B": 3.0, "C": 1.0}
    with pytest.raises(ValueError):
        dijkstra({"A": {"B": -1}}, "A")


def test_dynamic_programming():
    assert fibonacci(10) == 55
    assert number_of_ways_to_make_change(6, [1, 5]) == 2
    assert minimum_coins(7, [1, 5, 10]) == 3
    assert minimum_coins(3, [2]) == -1
    assert levenshtein_distance("kitten", "sitting") == 3
