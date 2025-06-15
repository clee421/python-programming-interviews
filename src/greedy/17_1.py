"""
Compute an Optimum Assignment of Tasks
"""


def solve(tasks: list[int]) -> int:
    sorted_tasks = sorted(tasks)

    longest = 0
    s, e = 0, len(sorted_tasks) - 1
    while s <= e:
        longest = max(longest, sorted_tasks[s] + sorted_tasks[e])
        s += 1
        e -= 1

    return longest


print(solve([5, 2, 1, 6, 4, 4]))
