#!/usr/bin/python3
"""Documentation for a square class"""


class Square():
    """Square class of a quadrilateral with four equal sides"""

    def __init__(self, size):
        """Sets the initial size of the new square object
        Args:
          size (int): the size of the suare once instance is created
        """
        self.__size = size
