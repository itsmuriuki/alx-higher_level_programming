#!/usr/bin/python3
"""Documentation for a rectangle class"""


class Rectangle:
    """Class for a Rectangle shape"""

    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instantiation of a rectangle
        Args:
            width (int, optional): the width of the rectangle
            height (int, optional): the height of the rectangle
        Raises:
            TypeError: if the values are not integers
            ValueError: if the value is negative
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of the instance
        Returns:
            the width of the instance of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the instance
        Args:
            value (int): the width of the instance
        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is negative
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the instance
        Returns:
            the height of the instance
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the instance
        Args:
            value (int): the height of the instance
        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is negative
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the instance"""

        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the instance"""

        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        """Functionality for printing and using str() functions"""

        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            if i is not self.__height - 1:
                rectangle.append('\n')
        return''.join(rectangle)

    def __repr__(self):
        """Creates a string that works with the eval() function"""

        string = []
        string.append("Rectangle(")
        string.append(str(self.__width) + ", " + str(self.__height) + ')')
        return ''.join(string)

    def __del__(self):
        """Functionality for when an instance is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangle areas
        Args:
            rect_1 (Rectangle): the first rectangular object
            rect_2 (Rectangle): the second rectangular object
        Raises:
            TypeError: if either rectangle are not instances of the
            Rectangle class
        Returns:
            rect_1 if rect_1's area is equal or greater than rect_2's
            rect_2 if rect_2's area is greater than rect_1's
        """

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.__width * rect_1.__height
        area2 = rect_2.__width * rect_2.__height

        if area1 == area2:
            return rect_1
        elif area1 > area2:
            return rect_1
        else:
            return rect_2
