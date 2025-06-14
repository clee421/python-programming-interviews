import math

"""
Merge Sorted Files
"""


class MinHeapOfList:
    def __init__(self):
        self._heap = []

    def add(self, _list: list[int]) -> None:
        self._heap.append(_list)
        curr = len(self._heap) - 1
        while curr != -1:
            parent = self._get_parent(curr)
            if parent == -1:
                break

            self._heap[parent], self._heap[curr] = self._heap[curr], self._heap[parent]
            curr = parent

    def pop(self) -> list[int]:
        curr = 0
        while curr != -1:
            child = self._get_child(curr)
            if child == -1:
                return self._heap.pop(curr)

            self._heap[child], self._heap[curr] = self._heap[curr], self._heap[child]
            curr = child

        raise Exception("we shouldn't get here")

    def _get_parent(self, i: int) -> int:
        """
                0
              1 | 2
          3 | 4   5 | 6

        parent = ceil(x / 2) - 1
        """

        if i == 0:
            return -1

        parent = int(math.ceil(i / 2)) - 1
        if self._heap[parent][0] <= self._heap[i][0]:
            return -1

        return parent

    def _get_child(self, i: int) -> int:
        """
                0
              1 | 2
          3 | 4   5 | 6

        child = (x * 2) + 1 / 2
        """

        if i >= len(self._heap) - 1:
            return -1

        child_1 = int(i / 2) + 1
        child_2 = int(i / 2) + 2

        child = -1
        if child_2 >= len(self._heap):
            child = child_1
        else:
            if self._heap[child_1][0] < self._heap[child_2][0]:
                child = child_1
            else:
                child = child_2

        if child == i:
            return -1

        return child


def solve(list_list_ints: list[list[int]]) -> list[int]:
    min_heap = MinHeapOfList()
    for lli in list_list_ints:
        min_heap.add(lli)

    min_list = []
    while len(min_heap._heap) > 0:
        next_list = min_heap.pop()
        min_list.append(next_list.pop(0))
        if len(next_list) > 0:
            min_heap.add(next_list)

    return min_list


print(
    solve(
        [
            [4, 5, 7],
            [0, 6],
            [0, 6, 28],
        ],
    )
)
