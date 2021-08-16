#!/usr/bin/python3
"""Documentation for a MyInt class based on int"""


class MyInt(int):
    """MyInt class which inherits from the int class"""

    def __init__(self, value):
        """Instantiation function

        Args:
            value (int): value to set the integer to
        """

        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        self.value = value

    def __eq__(self, y):
        """Equals to operator

        Returns:
            The result of x != y
        """

        return self.value != y

    def __ne__(self, y):
        """The not equals operator

        Returns:
            The result of x == y
        """

        return self.value == y
