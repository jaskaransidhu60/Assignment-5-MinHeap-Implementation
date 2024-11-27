# Name: JASKARAN SINGH SIDHU
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment:  5 MinHeap Implementation
# Due Date: 24 NOV 2025
# Description: Implements a minimum binary heap using a dynamic array.

from dynamic_array import DynamicArray

class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    """
    pass

class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        """
        self._heap = DynamicArray()
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MinHeap content in human-readable form
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return "HEAP " + str(heap_data)

    def add(self, node: object) -> None:
        """
        Add a new object to the MinHeap while maintaining heap property.
        """
        self._heap.append(node)
        child_idx = self._heap.length() - 1
        while child_idx > 0:
            parent_idx = (child_idx - 1) // 2
            if self._heap[child_idx] < self._heap[parent_idx]:
                self._heap.swap(child_idx, parent_idx)
                child_idx = parent_idx
            else:
                break

    def is_empty(self) -> bool:
        """
        Return True if the heap is empty; otherwise, return False.
        """
        return self._heap.length() == 0

    def get_min(self) -> object:
        """
        Return the minimum object without removing it from the heap.
        Raise MinHeapException if the heap is empty.
        """
        if self.is_empty():
            raise MinHeapException("Heap is empty.")
        return self._heap[0]

    def remove_min(self) -> object:
        """
        Return and remove the minimum object from the heap.
        Raise MinHeapException if the heap is empty.
        """
        if self.is_empty():
            raise MinHeapException("Heap is empty.")
        min_value = self._heap[0]
        last_value = self._heap.pop()
        if not self.is_empty():
            self._heap[0] = last_value
            self._percolate_down(0)
        return min_value

    def build_heap(self, da: DynamicArray) -> None:
        """
        Build a MinHeap from the provided DynamicArray.
        """
        self._heap = DynamicArray()
        for i in range(da.length()):
            self._heap.append(da[i])
        for i in range((self._heap.length() - 1) // 2, -1, -1):
            self._percolate_down(i)

    def size(self) -> int:
        """
        Return the number of items currently stored in the heap.
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        Clear the contents of the heap.
        """
        self._heap = DynamicArray()

    def _percolate_down(self, parent: int) -> None:
        """
        Helper method to maintain the heap property by percolating a node down.
        """
        while parent * 2 + 1 < self._heap.length():
            left_child = parent * 2 + 1
            right_child = parent * 2 + 2
            smallest_child = left_child

            if right_child < self._heap.length() and self._heap[right_child] < self._heap[left_child]:
                smallest_child = right_child

            if self._heap[parent] > self._heap[smallest_child]:
                self._heap.swap(parent, smallest_child)
                parent = smallest_child
            else:
                break

def heapsort(da: DynamicArray) -> None:
    """
    Sort the given DynamicArray in non-ascending order using Heapsort.
    """
    heap = MinHeap()
    heap.build_heap(da)
    for i in range(da.length() - 1, -1, -1):
        da[i] = heap.remove_min()

# ------------------- BASIC TESTING -----------------------------------------
if __name__ == '__main__':
    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
    print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
    print(h)

    print("\nPDF - remove_min example")
    print("-----------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, h.remove_min())

    print("\nPDF - heapsort example")
    print("----------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After: {da}")
