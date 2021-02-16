#!/usr/bin/python3
""" is_kind_of_class: function """


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class

    Args:
        obj (object): Object to be tested
        a_calss: To be checked
    Return: True if the object is an instance of, or if the object
                is an instance of a class that inherited
                from, the specified class
            False otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
    