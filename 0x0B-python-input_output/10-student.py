#!/usr/bin/python3
"""Documentation for a Student class"""

class Student:

    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation function for student 
        
        Args:
            first_name (str): the first name of the student
            last_name (str): the last name of the student
            age (int): the age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of an object or
        a dictionary representation of all string attributes
        
        Args:
            attrs (list): attributes to return

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
        

