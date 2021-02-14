#!/usr/bin/python3
""" Define a square """


def print_square(size):
    """ Print square

    Args:
        size: int size of the square
    Exceptions:
        TypeError: If size is not integer
        ValueError: if size < 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print()
