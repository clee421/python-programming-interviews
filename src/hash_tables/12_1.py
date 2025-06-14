"""
Test for Palindromic Permutations
"""


def solve(word_1: str, word_2: str) -> bool:
    c_dict: dict[str, int] = {}
    for c in word_1:
        v = c_dict.get(c, 0)
        c_dict[c] = v + 1

    for c in word_2:
        if c not in c_dict:
            return False

        c_dict[c] -= 1

    return not any(c_dict.values())


print(solve("edified", "deified"))
print(solve("edified", "deifid"))
print(solve("edifid", "deified"))
print(solve("abc", "efg"))
