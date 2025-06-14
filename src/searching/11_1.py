"""
Search a Sorted Array for First Occurrance of k
"""


def solve(_list: list[int], target: int) -> int:
    s, e = 0, len(_list) - 1
    while s <= e:
        mid = int((s + e) / 2)
        if _list[mid] == target:
            return mid

        if target < _list[mid]:
            e = mid - 1
        else:
            s = mid + 1

    return -1


print(solve([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 8))
print(solve([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 243))
print(solve([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 401))
print(solve([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], -14))
print(solve([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 108))
