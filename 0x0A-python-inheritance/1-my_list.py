#!/usr/bin/python3
"""1-my_list.py"""


class MyList(list):
    """Implementation of a list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
