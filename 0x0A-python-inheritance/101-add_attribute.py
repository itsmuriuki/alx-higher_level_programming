#!/usr/bin/python3
def add_attribute(obj, name, value):
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
