# LeetCode

Some leetcode solutions with tests.

## Structure

Each problem is stored under:

```text
src/leetcode/p<problem_number>_<problem_name>/
```

For example:

```text
src/leetcode/p0362_design_hit_counter/
```

## Adding a Problem

Use:

```bash
just add <number> <name>
```

For example:

```bash
just add 0362 design-hit-counter
```

This creates:

```text
src/leetcode/p0362_design_hit_counter/
├── __init__.py
├── solution.py
└── test_solution.py
```

`test_solution.py` is automatically initialized with:

```python
from .solution import *
```

## Running Tests

Run all tests:

```bash
just test
```

Run the tests for a specific problem:

```bash
just test src/leetcode/p0362_design_hit_counter
```
