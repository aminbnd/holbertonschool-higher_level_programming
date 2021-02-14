#!/usr/bin/python3
""" Defining matrix """


def matrix_divided(matrix, div):
    """ Divide elements of a matrix

    Execptions:
        TypeError:
        TypeError:
        TypeError:
        ZeroDivisionError:
    Returns:
        New matrix presenting the resulting values
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(el, int) or isinstance(el, float))
                    for el in [num for row in matrix for num in row])):
        raise TypeError(message)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
