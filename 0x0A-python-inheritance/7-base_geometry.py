#!/usr/bin/python3
""" defining BaseGeometry class """


class BaseGeometry:
    """ Class: BaseGeometry empty class """
    pass

    def area(self):
        """ area: Public instance method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Integer_validator: public instance method

        Args:
            name(str) string
            value(int): integer
        Exceptions:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
