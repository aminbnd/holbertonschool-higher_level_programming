#!/usr/bin/python3
""" Define function that prints name """


def say_my_name(first_name, last_name=""):
    """ Prints first name and last name

    Args:
        first_name: str
        last_name: str
    Exceptions:
        TypeError: If first name or last name (or both) is/are not str
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
