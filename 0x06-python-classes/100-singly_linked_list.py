#!/usr/bin/python3
# 100-singly_linked_list.py by Oluwaseun Akinbo


class Node:
    """Defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initializes the object class and attributes

        Args:
            data: The data stored in the node
            next_node: The next node in the list (default: None)
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retuns the data stored in the node.

        Args:
            value: The node data value
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Returns the next node in the list (None if tail).

        Args:
            value: next node value
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Represents a singly linked list."""
    def __init__(self):
        """Initializes the linked list

        Args:
            head: The head of the linked list
        """
        self.__head = None

    def __str__(self):
        """Prints the list"""
        current = self.__head
        output = ""
        while current:
            output += f"{current.data}\n"
            current = current.next_node
        return output[:-1]

    def sorted_insert(self, value):
        """Inserts a new node into the list in ascending order.

        Args:
            value: The node data value
        """
        new_node = Node(value)

        if not self.__head:
            self.__head = new_node
            return

        current = self.__head
        previous = None

        """Find the appropriate position to insert the node."""
        while current and current.data < value:
            previous = current
            current = current.next_node

        """Insert the new node before or after the current node."""
        if previous:
            previous.next_node = new_node
        else:
            self.__head = new_node
        new_node.next_node = current
