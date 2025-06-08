from .._utils.linked_lists import IntNode, create_int_linked_list

"""
Merge Two Sorted Lists
"""


def solve(l_list_1: IntNode | None, l_list_2: IntNode | None) -> IntNode | None:
    head = IntNode(-1, None)
    tail = head
    while l_list_1 is not None and l_list_2 is not None:
        val = None
        if l_list_1._val < l_list_2._val:
            val = l_list_1._val
            l_list_1 = l_list_1._next
        else:
            val = l_list_2._val
            l_list_2 = l_list_2._next

        new_node = IntNode(val, None)
        tail._next = new_node
        tail = tail._next

    rest_of_nodes = l_list_1
    if l_list_2 is not None:
        rest_of_nodes = l_list_2

    while rest_of_nodes is not None:
        new_node = IntNode(rest_of_nodes._val, None)
        rest_of_nodes = rest_of_nodes._next
        tail._next = new_node
        tail = tail._next

    return head._next


print(
    (
        solve(
            create_int_linked_list([1, 2, 3]),
            create_int_linked_list([2, 3, 4]),
        )
        or IntNode(-1)
    ).to_list()
)
