#!/usr/bin/python
""" is_same_class function """


def is_same_class(obj, a_class):
    """ is_same_class: finction
    Args:
        obj (obect):The object to be checked
        a_class (any type): attribute to be checked
    Return: True if the object is exactly an instance
        of the specified class
            False otherwise
    """
    if type(obj) is not a_class:
        return False
    return True
