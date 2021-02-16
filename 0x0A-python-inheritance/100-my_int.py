#!/usr/bin/python3
""" MyInt Class"""


class MyInt(int):
    """ MyInt: Class that inherits from int"""

    def __ne__(self, value):
        """ Overwrite != operator with == operator """
        return self.real == value

    def __eq__(self, value):
        """ Overwrite == operator with != operator"""
        return self.real != value
