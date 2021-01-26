#!/usr/bin/python3
""" Defining a Square """


class Square:
    """Square class
    Attributes: size (int): size of the squre """
    def __init__(self, size=0, position=(0, 0)):
        """size initialization"""
        self.__size = size
        self.position = position

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

    def my_print(self):
        """Printing a square"""
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                print("#" * self.size)

    @property
    def position(self):
        """Retrieve the position"""
        return self.position

    @position.setter
    def position(self, value):
        """Set the position"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
