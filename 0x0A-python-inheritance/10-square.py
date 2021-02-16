#!/usr/bin/python3
""" Defining Rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that iherits from BaseGeometry """

    def __init__(self, size):
        """ Initializing Square """
        self.__size = size
        self.integer_validator('size', self.__size)

    def area(self):
        """ Return the area of the rectangle """
        return self.__size ** 2

    def __str__(self):
        """ Return the print() and the str() representation of rectangle """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
