#!/usr/bin/python3
""" Defining Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that iherits from BaseGeometry """
    
    def __init__(self, width, height):
        """ Initializing Rectangle """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
