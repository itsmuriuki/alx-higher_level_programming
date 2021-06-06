#!/usr/bin/python3
"""Documentation for a square class"""


class Square():
    """Square class for a quadrilateral with four equal sides"""

    def __init__(self, size=0):
        """Sets the initial size values upon instantiation of the class"
           Throws errors if the value passed in is not an integer

        Args:
          size (int, optional): the size of the square object

        Raises:
          TypeErrror: when the value passed in is not an integer
          ValueError: when the value passed in is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the area of the square

        Returns:
           The area of the square
        """
        return self.__size ** 2
