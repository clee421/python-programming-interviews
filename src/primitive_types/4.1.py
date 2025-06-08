"""
Computing the parity of a word
"""


def solve(x: int) -> int:
    res = 0
    while x:
        inter = x & 1
        res ^= inter
        x >>= 1
    return res


solve(5)
