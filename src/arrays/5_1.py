"""
The dutch national flag problem
"""


def solve(arr: list[int], i: int) -> list[int]:
    # WTF are these problems..
    pivot = arr[i]
    s, e, count = 0, len(arr) - 1, 0
    j = 0
    while j <= e and s <= e:
        curr = arr[j]
        if curr < pivot:
            arr[j], arr[s] = arr[s], arr[j]
            s += 1
            j += 1
        elif curr > pivot:
            arr[j], arr[e] = arr[e], arr[j]
            e -= 1
        else:
            count += 1
            j += 1

    return arr


print(solve([3, 5, 1, 4, 3, 2, 4, 3], 1))
