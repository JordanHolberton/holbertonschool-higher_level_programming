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

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
