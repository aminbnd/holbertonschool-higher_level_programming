#!/usr/bin/python3
""" is_same_class function"""


def is_same_class(obj, a_class):
    """ is_same_class : function
    
    Args:
        obj (objecy): object to be tested
        a_class: To be checked
    Return:
        True if the object is exactly an
        instance of the specified class
        False otherwise
    """
    if type(obj) is not a_class:
        return False
    return True
