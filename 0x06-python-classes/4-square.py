#!/usr/bin/python3
"""Documentation for a class"""


class Square():
    """Square class for quadrilateral with four equal sides"""

    def __init__(self, size=0):
        """Sets the size of the square on instantiation
           Throws an error if the size passed in is not an integer

        Args:
           size (int, optional): the size of the square object

        Raises:
           TypeError: when the value passed in is not an integer
           ValueError: when the value passed in is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Retruns the current size of the object
        if called with a value, the setter function overwrites the
        current size with the size passed in

        Returns:
        size of the current object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Resets the size of the object with the value called

        Args:
        value (int): the new size of square object


        Raises:
          TypeError: When the value  passed in is not an integer
          ValueError: when the value passed in os less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise valueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
            """Returns the area of the current square objects"

            Returns:
               the area of the current square object
            """
            return self.__size ** 2
