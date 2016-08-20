# -*- coding: utf-8 -*-
"""Create a singly linked list."""
from __future__ import unicode_literals


class Node(object):
    """Create a node to store data."""

    def __init__(self, value, pointer=None):
        """Create an instance of a Node."""
        self.value = value
        self.pointer = pointer


class LinkedList(object):
    """Create a link list class to store strings of data."""

    def __init__(self, value_list=None):
        """Create an instance of a singly-linked list."""
        self.length = 0
        self.header = None
        try:
            for value in value_list:
                self.push(value)
        except TypeError:
            if value_list is not None:
                raise TypeError('Your input is not an itterable object.')

    def __len__(self):
        """Return the length of the linked list for the built in len."""
        return self.length

    def push(self, value):
        """Add a new node to the head of the linked list."""
        new_node = Node(value, self.header)
        self.header = new_node
        self.length += 1

    def size(self):
        """Return the length of the linked list."""
        return len(self)

    def pop(self):
        """Remove the first value off the head of the list and return it."""
        if self.length:
            pop_node = self.header
            self.header = pop_node.pointer
            self.length -= 1
            return pop_node.value
        else:
            raise IndexError('Cannot pop from an empty list.')

    def display(self):
        """Return a unicode string representing the list."""
        if self.length:
            return_str = '{0}{1}{2}'.format('(', self.header.value, ', ')
            current_node = self.header
            while current_node.pointer:
                my_value = current_node.pointer.value
                return_str += '{0}{1}'.format(my_value, ', ')
                current_node = current_node.pointer
            else:
                return_str = return_str.rstrip(', ') + ')'
            return return_str

    def search(self, val):
        """Return the node containing a 'val' in the list."""
        if self.length:
            if self.header.value == val:
                return self.header

            current_node = self.header
            while current_node.pointer:
                if current_node.pointer.value == val:
                    return current_node.pointer
                current_node = current_node.pointer

    def remove(self, remove_node):
        """Remove the given node from the list."""
        current_node = self.header
        while current_node.pointer:
            if current_node.pointer == remove_node:
                current_node.pointer = current_node.pointer.pointer
                self.length -= 1
                return
            current_node = current_node.pointer
