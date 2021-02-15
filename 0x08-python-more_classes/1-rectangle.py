#!/usr/bin/python3
""" Defining a class: Rectangle """

class Rectangle:
    """ Rectangle: class
    
    Attributes:
        width (int): Private attribute
        height (int): Private attribute
    """
    def __init__(self, width=0, height=0):
        """ Initializing Rectangle

        Args:
            width (int): The rectable width
            height (int): The rectangle height
        """
        self.__height = height
        self.__width = width
    
    @property
    def width(self):
        """ Retrieve width """
        return self.__width
    
    @width.setter
    def width(self, value):
        """ Set the width value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """ Retrieve height value """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ Set the height value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
