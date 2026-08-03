# Algorithms

Documented reference implementations of classical algorithms in Python. The repository is organized for systematic study: every implementation has a defined contract, type hints, complexity notes, and automated tests.

## Implemented modules

| Module | Implementations |
|---|---|
| Arrays | two-number sum, sorted squares, running sum, three-number sum, Kadane's algorithm |
| Searching | iterative binary search |
| Sorting | bubble, insertion, selection, merge, and quick sort |
| Strings | palindrome, Caesar cipher, first unique character, anagram, word reversal |
| Graphs | breadth-first search, depth-first search, Dijkstra's algorithm |
| Dynamic programming | Fibonacci, change counting, minimum coins, Levenshtein distance |

## Installation

Python 3.10 or later is required.

```bash
git clone https://github.com/ozsp12/algorithms.git
cd algorithms
python -m pip install -e ".[dev]"
python -m pytest
```

## Example

```python
from algorithms import binary_search, dijkstra, merge_sort

merge_sort([8, 3, 5, 1])
# [1, 3, 5, 8]

binary_search([1, 3, 5, 8], 5)
# 2

dijkstra({"A": {"B": 4, "C": 1}, "C": {"B": 2}, "B": {}}, "A")
# {"A": 0.0, "B": 3.0, "C": 1.0}
```

## Study roadmap

The original collection of 200 study problems is preserved in [ROADMAP.md](ROADMAP.md). Difficulty bands are treated as guidance rather than an intrinsic property of a problem; implementation status should be established by the presence of documented code and tests.

See [CONTRIBUTING.md](CONTRIBUTING.md) for implementation standards and [REFERENCES.md](REFERENCES.md) for canonical sources.

## Author

**Dr. Osvaldo L. Santos-Pereira** — [Academic webpage](https://ozsp12.github.io/) · [Lattes](http://lattes.cnpq.br/6730251976463283) · [ORCID](https://orcid.org/0000-0003-2231-517X) · [Google Scholar](https://scholar.google.com/citations?user=HIZp0X8AAAAJ&hl=en) · [ResearchGate](https://www.researchgate.net/profile/Osvaldo-Santos-Pereira) · [GitHub](https://github.com/ozsp12) · [LinkedIn](https://www.linkedin.com/in/ozsp12) · [Substack](https://substack.com/@olsp1982) · [Medium](https://medium.com/@ozsp12) · [YouTube](https://www.youtube.com/@ozlsp12) · [X](https://x.com/ozsp12)
