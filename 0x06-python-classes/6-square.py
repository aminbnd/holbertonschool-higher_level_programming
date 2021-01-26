#!/usr/bin/python3
""" Defining a Square """


class Square:
    """Square class
    Attributes: size (int): size of the squre """
    def __init__(self, size=0, position=(0, 0)):
        """size initialization
        position initialization"""
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
            print("\n" * self.__position[1], end="")
            for i in range(self.size):
                print(" " * self.__position[0], end="")
                print("#" * self.size)

    @property
    def position(self):
        """ Retrieve """
        return self.position

    @position.setter
    def position(self, value):
        """ set the position """
        if type(value) == tuple and len(value) == 2 and \
           type(value[0]) is int and value[0] >= 0 and \
           type(value[1]) is int and value[1] >= 0:
            self.__position = value
        else:
            raise("position must be a tuple of 2 positive integers")
