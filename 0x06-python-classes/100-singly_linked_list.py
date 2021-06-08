#!/usr/bin/python3
"""Documentation for singly linked list class"""


class Node():
    """Node class for a singly-linked list"""

    def __init__(self, data, next_node=None):
        """instantiation of a singly-linked list node

        Args:
          data (int): data contained in the node
          next_node (Node, optional): the next node of the list

        Raises:
          TypeError: if the data is not an integer of next_node is not
          a Node instance
        """

        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data

        if next_node is None or isinstance(next_node, Node):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """Returns the data value in the current node

        Returns:
          data value contained in current node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data value of the current node

        Args:
          data (int): the new data value of the node

        Raises:
          TypeError: when the data value is not an integer
        """

        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data     @property

    @property
    def next_node(self):
        """Retrives the next_node value for the current node

        Returns:
          the next_node of the current node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets a new next_node of the current node

        Args:
          value (Node): the new node

        Raises:
          TypeError: if the next_node is not a Node instance
        """

        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_npde must be a Node object")


class SinglyLinkedList():
    """Singly-linked list class - start out empty"""

    def __init__(self):
        """Initializes an empty singly linked list object"""

        self.__head = None

    def sorted_insert(self, value):
        """Inserts a Node into the linked list in a sorted fashion

        Args:
          value (int): the Node value

        Raises:
          TypeError:if the value supplied to the node is not an integer
        """

        if type(value) != int:
            raise TypeError("data must be an integer")
        temp = None
        iterator = self.__head
        new_node = Node(value)
        if iterator is None:
            new_node.__next_node = None
            self.__head = new_node

        else:
            while iterator is not None and value > iterator.data:
                temp = iterator
                iterator = iterator.__next_node
            if temp is None:
                new_node.__next_node = self.__head
                self.__head = new_node
            else:
                temp.__next_node = new_node
                new_node.__next_node = iterator

    def __str__(self):
        """Default printing operation for the class when print() is called"""

        linked_list = []
        iterator = self.__head
        while iterator is not None:
            linked_list.append(iterator.data)
            iterator = iterator.__next_node
        return ('\n'.join(str(i) for i in linked_list))
