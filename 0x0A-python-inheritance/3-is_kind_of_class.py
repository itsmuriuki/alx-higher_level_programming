#!/usr/bin/python3
"""Documentation for an inherited class checker"""


def is_kind_of_class(obj, a_class):
    """Checks if object is an instance of or an instance of a class that
       inherited from a specified class

    Returns:
        True if the object is an instance, False otherwise
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
