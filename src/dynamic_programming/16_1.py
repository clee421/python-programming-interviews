"""
Count the Number of Score Combinations
"""


def solve(score: int) -> int:
    score_points = [
        2,  # safety
        3,  # field goal
        7,  # touch down
    ]

    dp = [0]
    for i in range(1, score):
        possible_ways = 0
        for p in score_points:
            if i >= p and dp[i - p] != 0:
                possible_ways += dp[i - p]
            elif i == p:
                possible_ways += 1

        dp.append(possible_ways)

    return dp[-1]


print(solve(12))
