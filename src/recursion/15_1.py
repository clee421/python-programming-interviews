"""
The Towers of Hanoi Problem
"""


def solve(n: int = 2) -> int:
    # (calvinl) i don't like this problem because it's not really recursion
    towers = [
        [x for x in range(1, n + 1)],
        [],
        [],
    ]
    print(towers)

    return 0


print(solve(3))
