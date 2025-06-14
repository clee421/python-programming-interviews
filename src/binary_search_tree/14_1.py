from src._utils.binary_search_trees import create_int_binary_search_tree, IntTreeNode

"""
Test if a Binary Tree Satisfies the BST Property
"""


def solve(root: IntTreeNode | None) -> bool:
    if root is None:
        return True

    def is_BST(node: IntTreeNode | None, less: int | None, greater: int | None) -> bool:
        if node is None:
            return True

        if node._left is None and node._right is None:
            return True

        if node._left is not None and node._left._val > node._val:
            return False

        if node._right is not None and node._right._val < node._val:
            return False

        if less is not None:
            if node._val > less:
                return False

            if node._left is not None and node._left._val > less:
                return False

            if node._right is not None and node._right._val > less:
                return False

        if greater is not None:
            if node._val < greater:
                return False

            if node._left is not None and node._left._val < greater:
                return False

            if node._right is not None and node._right._val < greater:
                return False

        return is_BST(node._left, node._val, None) and is_BST(node._right, None, node._val)

    return is_BST(root, None, None)


print(solve(create_int_binary_search_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
