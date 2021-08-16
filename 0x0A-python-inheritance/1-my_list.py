#!/usr/bin/python3
"""Documentation of a class MyList that inherits from list"""


class MyList(list):

    """MyList class that inherits from the list class"""

    def print_sorted(self):
        """Function sorts the current instance of MyList"""

        print(sorted(self))
    
