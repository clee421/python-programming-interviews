from .._utils.binary_trees import IntTreeNode, create_int_binary_tree

"""
Test if B-Tree is Balanced
"""


def solve(root: IntTreeNode | None) -> bool:
    if root is None:
        return True

    def _get_tree_height(tree_node: IntTreeNode | None) -> int:
        if tree_node is None:
            return 0

        return max(_get_tree_height(tree_node._left), _get_tree_height(tree_node._right)) + 1

    left = _get_tree_height(root._left)
    right = _get_tree_height(root._right)

    return abs(left - right) < 2


print(
    solve(
        create_int_binary_tree(
            {
                "val": 3,
                "left": {
                    "val": 4,
                    "left": {
                        "val": 6,
                        "left": None,
                        "right": None,
                    },
                    "right": {
                        "val": 7,
                        "left": None,
                        "right": None,
                    },
                },
                "right": {
                    "val": 5,
                    "left": {
                        "val": 8,
                        "left": None,
                        "right": None,
                    },
                    "right": {
                        "val": 9,
                        "left": None,
                        "right": None,
                    },
                },
            },
        ),
    )
)
