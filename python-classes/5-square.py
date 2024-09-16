#!/usr/bin/python3
"""Function for define a square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """
        initialize a new square


        Args:
        size (int): Size of the square
        """
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        for i in range(0, self.__size):
            [print('#', end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
