#!/usr/bin/python3
"""
Modul that contains only matrix_mul(...) function
"""


def matrix_mul(m_a, m_b):
    """
    matrix_mul: function  that maultiply two matrix 

    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix
    Exceptions:
        TypeError: if m_a or m_b is not a list
        TypeError: if m_a or m_b is not list of lists
        ValueError: if m_a or m_b is empty
        TypeError: if one element of those list of lists is not a number
        TypeError: if m_a or m_b is not a rectangle
        ValueError: If m_a and m_b can’t be multiplied
    Return (list of lists): the resulting matrix
    """
    # TypeError if m_a is not a list
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    
    # TypeError if m_b is not a list
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    
    # TypeError if m_a is not a list of lists
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
    
    # TypeError if m_b is not a list of lists
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
    
    # ValueError if m_a is empty
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    
    # ValueError if m_b is empty
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    
    # ValueError if m_a is empty
    for i in m_a:
        if len(i) == 0:
            raise ValueError("m_a can't be empty")
    
    # ValueError if m_b is empty
    for i in m_b:
        if len(i) == 0:
            raise ValueError("m_b can't be empty")
    
    # TypeError if elements of m_a are not numbers
    for i in m_a:
        if not all(type(j) is int or type(j) is float for j in i):
            raise TypeError("m_a should contain only integers or floats")
    
    # TypeError if elements of m_b are not numbers
    for i in m_b:
        if not all(type(j) is int or type(j) is float for j in i):
            raise TypeError("m_b should contain only integers or floats")
    
    # TypeError if elements of m_a are not of the same size
    for i in m_a:
        if len(i) != len(m_a[0]):
            raise  TypeError("each row of m_a must be of the same size")
    
    # TypeError if elements of m_a are not of the same size
    for i in m_b:
        if len(i) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    #ValueError if m_a and m_b can't be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # List comprehesion to multiply the 2 matrix in a new matrix
    new = [[sum(a*b for a, b in zip(i, j)) for j in zip(*m_b)] for i in m_a]
    return new
