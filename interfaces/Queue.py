import logging
from functools import total_ordering


class Queue(object):
    """
    A queue implementation, with the following attributes

     - First in, first out

    """

    def __init__(self):
        pass

    def add(self, element):
        """
        Add the element to the data structure
        :param element: An element to be added
        :return: self
        :rtype: Queue
        """
        pass

    def remove(self):
        """
        Remove the element from the head of the data structure
        :return: self
        :rtype: Queue
        """
        pass

    def peak(self):
        """
        Return the value of head of the data structure
        :return: Element at the head of the list.
        """
        pass

    def contains(self, query_element):
        """
        Determine if the query element is in the linked list
        :param query_element: An element to check for in the data structure
        :return: A boolean, indicating whether the query element occurs in the data structure at least once
        :rtype: bool
        """
        pass

    def size(self):
        """
        Returns the number of elements in the list
        :return: The number of elements in the list
        :rtype: int
        """
        pass

