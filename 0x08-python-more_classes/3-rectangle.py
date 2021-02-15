#!/usr/bin/python3
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
        self.height = height
        self.width = width

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
        """ print the rectangle with # character
            Return:
                Printed rectangle with # character
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("#"*self.__width + "\n")*self.height

