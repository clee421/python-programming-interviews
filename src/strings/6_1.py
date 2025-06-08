"""
Interconvert Strings and Integers
"""


def solve(val: int | str) -> tuple[int, str]:
    digit_map = {k_str: k_int for (k_str, k_int) in zip(list("0123456789"), [v for v in range(10)])}

    # Cannot use int(val)
    def _str_to_int(str_val: str) -> int:
        pos = True
        if str_val[0] == "-":
            pos = False

        res = None
        for c in list(str_val):
            if c not in digit_map:
                continue

            if res is None:
                res = digit_map[c]
            else:
                res *= 10
                res += digit_map[c]

        if res is None:
            res = 0

        if not pos:
            res *= -1

        return res

    def _int_to_str(int_val: int) -> str:
        return f"{int_val}"

    if isinstance(val, str):
        return (_str_to_int(val), val)

    return (val, _int_to_str(val))


print(solve("123"))
print(solve("-123"))
print(solve("+123"))
