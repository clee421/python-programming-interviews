"""
Compute the Intersection of Two Sorted Arrays
"""


def solve(list_1: list[int], list_2: list[int]) -> list[int]:
    res_set = set()
    set_1 = set(list_1)
    for n in list_2:
        if n in set_1:
            res_set.add(n)

    return sorted(list(res_set))


print(
    solve(
        [5, 5, 6, 8, 8, 9, 10, 10],
        [2, 3, 3, 5, 5, 6, 7, 7, 8, 12],
    )
)
