import logging
from functools import total_ordering


class LinkedList(object):
    """
    A linked list implementation, with the following attributes

     - Singly linked
     - First in, first out
     - New elements added to end of list
     - Elements removed from beginning of list

    API roughly based on https://docs.oracle.com/javase/7/docs/api/java/util/LinkedList.html

    """

    def __init__(self):
        self.size = None
        pass

    def add(self, element):
        """
        Add the element to the end of the list
        :param element: An element to be added
        :return: self
        :rtype: LinkedList
        """
        pass

    def remove(self):
        """
        Remove the element from the isHead of the list
        :return: self
        :rtype: LinkedList
        """
        pass

    def peak(self):
        """
        Return the value of the isHead of the list, without removing it from the list
        :return: Element at the isHead of the list.
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

