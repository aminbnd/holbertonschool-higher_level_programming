#!/usr/bin/python3
"""
Lazy matrix multiplication
 multiply two matrices 

 """


import numpy as n

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices

    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix
    Return:
        new_mat (list of lists): the resulting matrix
    """
    new_mat = n.matmul(m_a, m_b)
    return new_mat
