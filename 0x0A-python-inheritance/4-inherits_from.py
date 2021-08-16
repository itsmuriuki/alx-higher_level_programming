#!/usr/bin/python3
"""Documentation for inheritance checker"""


def inherits_from(obj, a_class):
    """Checks if object is an instance of a class that inherited from
       a specified class

    Returns:
        True if object is an instance, False otherwise
    """

    if issubclass(obj.__class__, a_class) and type(obj) != a_class:
        return True
    else:
        return False
