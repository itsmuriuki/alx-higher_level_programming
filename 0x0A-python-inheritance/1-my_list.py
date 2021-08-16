#!/usr/bin/python3
""" Documentation for simple MyList class that inherits from the list class"""


class MyList(list):

    """MyList class that inherits from the list class"""

    def print_sorted(self):
        """Function sorts the current instance of MyList"""

        print(sorted(self))
