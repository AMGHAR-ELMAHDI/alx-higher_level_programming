#!/usr/bin/python3
"""12-pascal_triangle Module
"""


def fact(i):
    """Returns the factorial of a given integer i.e. i!"""
    if i == 0:
        return 1
    return i * fact(i - 1)


def comb(n, r):
    """Returns the result of nCr"""
    return fact(n) / (fact(r) * fact(n - r))


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    return [[int(comb(x, i)) for i in range(x + 1)] for x in range(n)]
