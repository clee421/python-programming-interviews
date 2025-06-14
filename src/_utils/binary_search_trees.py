from typing import Optional


class IntTreeNode:
    def __init__(self, val: int, left: Optional["IntTreeNode"], right: Optional["IntTreeNode"]):
        self._val = val
        self._left = left
        self._right = right


def create_int_binary_search_tree(int_list: list[int]) -> IntTreeNode | None:
    if not int_list:
        return None

    mid = int(len(int_list) / 2)
    root_node = IntTreeNode(
        val=int_list[mid],
        left=create_int_binary_search_tree(int_list[0:mid]),
        right=create_int_binary_search_tree(int_list[mid + 1 :]),
    )

    return root_node
