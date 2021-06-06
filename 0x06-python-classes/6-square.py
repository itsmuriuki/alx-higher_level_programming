#!/usr/bin/python3
"""Documentation of a square class"""


class Square():
    """Square class for quadrilateral with four equal sides"""

    def __init__(self, size=0, position=(0, 0)):
        """Sets the initial size and position of an instantiated object
        Throws an error when size is not integer or when position is not a
        tuple containing two integers

        Args:
          size (int, optional): the size of the square object
          position (tuple, optional): the poition of the object when printed

        Raises:
          TypeError: when the value passed is not an nteger or a two integer
          tuplet
        ValueError: when the value passsed is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """Returns the current size of the square object

        Returns:
           the current size of the square object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """resets the size of the square object

        Args:
          value (int):the size of the square object to reset to

        Raises:
          TypeError: when the value passed is not an integer or a two integer
          tuplet
          ValueError: when the value passed is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Returns the current position of the square object

        Returns:
           the current position of the square object
        """
        return self.__position

    @position.setter
    def position(self, value):
        """resets the position of the square object

        Args:
          value (tuple): a tuple of two integers defining the position

        Raises:
          TypeError: when the value passed is not an integer or a two integer
          tuplet
          ValueError: when the value passed is less than 0

        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[1] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of the current square
        Returns:
          the current area of the square object
        """

        return self.__size ** 2

    def my_print(self):
        """Prints the current square object with a size and at a position"""
        if self.__size == 0:
            print()
            return

        if self.__position[0] >= 0 and self.__position[1] >= 0:
            for height in range(self.__position[1]):
                print()

        for rows in range(self.__size):
            for spaces in range(self.__position[0]):
                print(' ', end='')
            for columns in range(self.__size):
                print('#', end='')
            print()
