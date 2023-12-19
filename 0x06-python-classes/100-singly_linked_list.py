#!/usr/bin/python3

class Node:
    """Defines node of singly linked list."""


    def __init__(self, data, next_node=Node):
        """Initializes Node instance.

        Args:
            data: integer representing data of node
            next_node: node representing the next node in list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for the data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for the data attribute.

        Args:
            value: An in representing the data for node

        Raises:
            TypeError: if value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def nex_node(self):
        """Getter for the next node."""
        return slef.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for the next node.

        Args:
            value: value to be set on the next node of list

        Raises:
            TypeError: if value is not node or object node
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

    class SinglyLinkedList:
        """Definition of singly linked list."""

        def __init__(self):
            """Initializes an instance of singlylinked list with empty list"""
            self.head = None

        def sorted_insert(self, value):
            """Inserts a new Node into position in list

            Args:
                value: integer representing data for newly added node
            """
            new_node = Node(value)

            if self.head is None or value < self.head.data:
                new_node.next_node =  self.head
                self.head = new_node
            else:
                current = self.head
                while current.next_node is not None and current.next_node.data
                < value:
                    current = current.next_node
                new_node.next_node = current.next_node
                current.next_node = new_node

