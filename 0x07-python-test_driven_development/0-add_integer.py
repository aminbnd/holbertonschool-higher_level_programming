#!/usr/bin/python3
""" Definition of a function returning the sum of two integers"""


def add_integer(a, b=98):
    """ Returns a + b
    Raises:
        TypeError: If a or b are is not integer or float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
