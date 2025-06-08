from typing import Optional


class IntNode:
    def __init__(self, val: int, next: Optional["IntNode"] = None):
        self._val = val
        self._next = next

    def to_list(self) -> list[int]:
        _list = []
        curr: Optional["IntNode"] = self
        while curr is not None:
            _list.append(curr._val)
            curr = curr._next  # noqa

        return _list


def create_int_linked_list(arr: list) -> IntNode | None:
    prev = None
    for e in reversed(arr):
        new_node = IntNode(e, prev)
        prev = new_node

    return prev
