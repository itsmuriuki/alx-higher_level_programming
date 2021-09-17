#!/usr/bin/python3
"""Documentation for a Student class"""

class Student:

    """The student class"""

    def __init__(self, first_name, last_name, age):
        """Instantitation function for students class
        
        Args: 
            first_name (str): the first name of the student 
            last_name (str): the last name of the student 
            age (int): the age of the student

        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the instance
        
        Returns:
            dictionary representation of the instance
        """

        return self.__dict__
