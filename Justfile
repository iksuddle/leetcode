test path="":
    uv run pytest {{path}} -v

add number name:
    #!/usr/bin/env bash
    set -euo pipefail

    name="{{name}}"
    slug="${name//-/_}"
    slug="${slug// /_}"
    slug="${slug,,}"

    dir="src/leetcode/p{{number}}_${slug}"

    mkdir -p "$dir"
    touch "$dir/__init__.py"
    touch "$dir/solution.py"
    printf 'from .solution import *\n' > "$dir/test_solution.py"

    echo "Created $dir"
