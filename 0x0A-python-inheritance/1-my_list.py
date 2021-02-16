#!/usr/bin/python3
"""
MyList class that iherit list
"""


class MyList(list):
    """ MyList: Class """
    def print_sorted(self):
        """ Prints sorted list
        Return: sorted list
        """
        return print(sorted(self))
