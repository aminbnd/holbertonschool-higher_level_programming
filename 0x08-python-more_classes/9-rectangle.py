#!/usr/bin/python3
""" Defining a class: Rectangle """


class Rectangle:
    """ Rectangle: class

    Attributes:
        width (int): Private attribute
        height (int): Private attribute
    """
    print_symbol = '#'
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initializing Rectangle

        Args:
            width (int): The rectable width
            height (int): The rectangle height
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Class Method that calculates the Area of the rectangle

        Return:
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Class Method that calculates the perimeter of the rectangle

        Return:
            The perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """
        print the rectangle with # character
            Return:
                Printed rectangle with # character
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ((str(self.print_symbol)*self.__width + "\n")*self.height)[:-1]

    def __repr__(self):
        """ Provides representation of the rectangle

        Return:
            The representation of the rectangle (str)
        """
        return ('Rectangle({}, {})'.format(self.__width, self.__height))

    def __del__(self):
        """ Delet instance and prints message"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compares two rectangles
        Args:
            rect_1: first rect
            rect_2: second rect
        Exceptions:
            TypeError: if rect_1 or rect_2 is not instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """ Makes a square from a rectangle
        Args:
            size (int): size of the rectangle
        Return:
            New rectangle with width == size
        """
        return cls(size, size)
