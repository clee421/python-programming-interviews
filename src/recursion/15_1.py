"""
The Towers of Hanoi Problem
"""


def solve(n: int = 2) -> list[tuple[int, int]]:
    """
    Return the sequence of moves (from-peg, to-peg) that solves
    the Towers of Hanoi puzzle for *n* rings.

    Pegs are numbered 1, 2, 3.
    """

    # (calvinl) I asked chatgpt to solve this problem because i think it's stupid
    def compute_steps(rings: int, from_peg: int, to_peg: int) -> list[tuple[int, int]]:
        if rings == 0:
            return []

        spare = 6 - from_peg - to_peg
        moves: list[tuple[int, int]] = []

        moves += compute_steps(rings - 1, from_peg, spare)
        moves.append((from_peg, to_peg))
        moves += compute_steps(rings - 1, spare, to_peg)

        return moves

    return compute_steps(n, 1, 3)


print(solve(3))
