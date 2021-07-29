#!/usr/bin/python3
"""Documentation for a square printing function"""

def print_square(size):
    """Function will print a square of length size

    Args:
       size (int): the side legth of the square

    Raises:
       TypeError: when the size passed in is not an integer
       ValueError: when the size is less than 0 (ie negative)
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >=0")
    for i in range(size):
        for i in range(size):
            print('#', end='')
        print()
