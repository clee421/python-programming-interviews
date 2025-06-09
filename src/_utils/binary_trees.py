from typing import Optional, TypedDict


class IntTreeNode:
    def __init__(self, val: int, left: Optional["IntTreeNode"], right: Optional["IntTreeNode"]):
        self._val = val
        self._left = left
        self._right = right


class TreeDict(TypedDict):
    val: int
    left: "TreeDict" | None
    right: "TreeDict" | None


def create_int_binary_tree(tree_dict: TreeDict | None = None) -> IntTreeNode | None:
    if tree_dict is None:
        return None

    head_node = IntTreeNode(
        val=tree_dict["val"],
        left=create_int_binary_tree(tree_dict["left"]),
        right=create_int_binary_tree(tree_dict["right"]),
    )

    return head_node
