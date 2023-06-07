#!/usr/bin/python3
"""2-square.py"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """
        Creates an instance of Square
        Args:
            size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = 
