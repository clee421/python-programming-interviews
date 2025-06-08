"""
Buy and sell stock once
"""


def solve(arr: list[int]) -> int:
    curr_mins = [2**1000]
    curr_maxs = [-1]
    for e in arr:
        curr_mins.append(min(curr_mins[-1], e))
        curr_maxs.append(max(curr_maxs[-1], e))

    max_profit = 0
    for i in range(len(curr_mins)):
        max_profit = max(max_profit, curr_maxs[i] - curr_mins[i])

    return max_profit


print(solve([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
