# Name: Jaksran singh sidhu
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Helper for MinHeap Implementation
# Description: Implements a resizable array.

class DynamicArray:
    def __init__(self):
        """
        Initialize a new dynamic array
        """
        self._data = [None] * 4
        self._size = 0
        self._capacity = 4

    def __str__(self) -> str:
        """
        Return the content of the dynamic array in a human-readable format
        """
        return f"DYN_ARR Size/Cap: {self._size}/{self._capacity} " + str([self._data[i] for i in range(self._size)])

    def length(self) -> int:
        """
        Return the number of elements in the dynamic array
        """
        return self._size

    def append(self, value: object) -> None:
        """
        Add an element to the end of the dynamic array
        """
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = value
        self._size += 1

    def get_at_index(self, index: int) -> object:
        """
        Get the value at the given index
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Set the value at the given index
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        self._data[index] = value

    def pop(self) -> object:
        """
        Remove the last element in the dynamic array and return it
        """
        if self._size == 0:
            raise IndexError("Array is empty")
        value = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return value

    def swap(self, index1: int, index2: int) -> None:
        """
        Swap the elements at the given indices
        """
        if index1 < 0 or index1 >= self._size or index2 < 0 or index2 >= self._size:
            raise IndexError("Index out of bounds")
        self._data[index1], self._data[index2] = self._data[index2], self._data[index1]

    def _resize(self, new_capacity: int) -> None:
        """
        Resize the array to the new capacity
        """
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def __getitem__(self, index: int) -> object:
        """
        Get the value at the given index using the bracket operator
        """
        return self.get_at_index(index)

    def __setitem__(self, index: int, value: object) -> None:
        """
        Set the value at the given index using the bracket operator
        """
        self.set_at_index(index, value)
