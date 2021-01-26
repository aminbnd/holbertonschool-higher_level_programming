#!/usr/bin/python3
""" Defining a Square """


class Square:
    """Square class
    Attributes: size (int): size of the squre """
    def __init__(self, size=0):
        """size initialization"""
        self.__size = size

    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """ Retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
