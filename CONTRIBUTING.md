# Contributing

Contributions should make the repository more rigorous, reproducible, and useful for study.

1. Create a focused branch from `main`.
2. Place the implementation in the module matching its algorithmic family.
3. Add type hints and a docstring stating behavior, assumptions, and asymptotic complexity.
4. Avoid mutating caller-owned inputs unless the function explicitly documents mutation.
5. Add tests for the ordinary case and relevant boundary cases: empty input, singleton input, duplicates, unreachable states, or invalid parameters.
6. Run `python -m pytest` before opening a pull request.

Prefer clear reference implementations over clever compression. If two standard variants have materially different complexity or behavior, implement and document them separately.
