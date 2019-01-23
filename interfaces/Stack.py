import logging
from functools import total_ordering


class Stack(object):
    """
    A stack implementation, with the following attributes

     - First in, last out

    """

    def __init__(self):
        pass

    def add(self, element):
        """
        Add the element to the stack
        :param element: An element to be added
        :return: self
        :rtype: Stack
        """
        pass

    def remove(self):
        """
        Remove the element from the head of the stack
        :return: self
        :rtype: Stack
        """
        pass

    def peak(self):
        """
        Return the value of head of the stack
        :return: Element at the head of the list.
        """
        pass

    def size(self):
        """
        Returns the number of elements in the list
        :return: The number of elements in the list
        :rtype: int
        """
        pass

