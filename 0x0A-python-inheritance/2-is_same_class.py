#!/usr/bin/python3
"""Documentation for a class instance checker"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class

    Returns:
        True if object is an instance, False otherwise
    """

    if type(obj) == a_class:
        return True
    else:
        return False
