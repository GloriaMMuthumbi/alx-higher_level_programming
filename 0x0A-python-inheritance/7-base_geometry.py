#!/usr/bin/python3
"""
defines empty BaseGeometry class
"""


class BaseGeometry:
    """ represents class basegeometry """
    def area(self):
        """
        Raises:
            Exception: area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value

        Args:
            name (str): name of the value
            value : vlaue to be validated

        Raises:
            TypeError: if the value is not an integer
            ValueError: if value is less than or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')

        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
