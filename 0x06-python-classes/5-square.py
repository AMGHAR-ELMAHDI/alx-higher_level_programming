#!/usr/bin/python3
"""5-square.py"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """
        Creates an instance of Square
        Args:
            size: size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Sets and gets the value of private size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Finds area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using #
        """
        for i in range(self.__size):
            print("#" * self.__size)

        if (self.__size == 0):
            print()
