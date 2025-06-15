"""
Search a Maze
"""

DIRECTIONS: list[tuple[int, int]] = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def solve(maze: list[list[str]]) -> bool:
    s, e = (-1, -1), (-1, -1)
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "s":
                s = (i, j)

            if maze[i][j] == "e":
                e = (i, j)

    seen = set()
    queue: list[tuple[int, int]] = [s]
    while queue:
        curr = queue.pop(0)
        if curr == e:
            return True

        for d in DIRECTIONS:
            x, y = curr[0] + d[0], curr[1] + d[1]

            if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[x]):
                continue

            if (x, y) in seen:
                continue

            queue.append((x, y))
            seen.add((x, y))

    return False


print(
    solve(
        [
            ["x", ".", ".", ".", ".", ".", "x", "x", ".", "e"],
            [".", ".", "x", ".", ".", ".", ".", ".", ".", "."],
            ["x", ".", "x", ".", ".", "x", "x", ".", "x", "x"],
            [".", ".", ".", "x", "x", "x", ".", ".", "x", "."],
            [".", "x", "x", ".", ".", ".", ".", ".", ".", "."],
            [".", "x", "x", ".", ".", "x", ".", "x", "x", "."],
            [".", ".", ".", ".", "x", ".", ".", ".", ".", "."],
            ["x", ".", "x", ".", "x", ".", "x", ".", ".", "."],
            ["x", ".", "x", "x", ".", ".", ".", "x", "x", "x"],
            ["s", ".", ".", ".", ".", ".", ".", "x", "x", "."],
        ]
    )
)
