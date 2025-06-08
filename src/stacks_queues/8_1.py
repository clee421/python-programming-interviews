"""
Implement Stack with Max API
"""


class IntStack:
    def __init__(self):
        self.max = None
        self._stack = []

        self._max_tracker = []

    def pop(self) -> int | None:
        if len(self._stack) < 1:
            return None

        v = self._stack.pop()
        self._max_tracker.pop()

        self.max = None
        if len(self._max_tracker) > 0:
            self.max = self._max_tracker[-1]

        return v

    def push(self, val: int) -> None:
        self._stack.append(val)
        if len(self._max_tracker) < 1:
            self._max_tracker.append(val)
        else:
            self._max_tracker.append(max(self._max_tracker[-1], val))
        self.max = self._max_tracker[-1]


def solve() -> bool:
    stack = IntStack()

    if stack.pop() is not None:
        return False

    stack.push(5)
    stack.push(2)
    stack.push(1)
    if stack.max != 5:
        return False

    stack.push(8)
    if stack.max != 8:
        return False

    stack.pop()
    if stack.max != 5:
        return False

    return True


print(solve())
