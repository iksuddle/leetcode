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
    package="p{{number}}_${slug}"

    mkdir -p "$dir"
    touch "$dir/solution.py"
    printf 'from leetcode.%s import solution\n' "$package" > "$dir/test_solution.py"

    echo "Created $dir"
