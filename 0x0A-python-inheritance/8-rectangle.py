#!/usr/bin/python3
"""Documentation for BaseGeometry class"""


class BaseGeometry:

    """Base Geometry class that is empty"""

    def area(self):
        """Area function for geometry"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer value

        Args:
            name (str): the string name
            value (int): the value to be validated

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than or equal to 0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):

    """Rectangle class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Instantiation function

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
