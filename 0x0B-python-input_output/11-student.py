#!/usr/bin/python3
"""Documentation for a Student class"""


class Student:

    """The Student class"""

    def __init__(self, first_name, last_name, age):
        """Instatiation function for Student class

        Args:
            first_name (str): the first name of the student
            last_name (str): the last name of the student
            age (int): the age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of the object

        Args:
            attrs (list): the attributes to include in the dictionary

        Returns:
            A dictionary representation of the object
        """

        if not isinstance(attrs, list):
            return self.__dict__
        for var in attrs:
            if not isinstance(var, str):
                return self.__dict__
        string_dict = {}
        for string in attrs:
            if string in self.__dict__.keys():
                string_dict[string] = self.__dict__[string]
        return string_dict

    def reload_from_json(self, json):
        """Replaces the attributes in the instance

        Args:
            json (dict): a dictionary of values to replace
        """

        keys = list(json.keys())
        for key in keys:
            if key in self.__dict__.keys():
                self.__dict__[key] = json[key]