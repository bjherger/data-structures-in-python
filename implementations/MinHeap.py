import logging
from functools import total_ordering


class MinHeap(object):
    """
    A min heap implementation, with the following attributes

     - Complete tree
     - Root is minimum of all values

    """

    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, element):
        """
        Add the element to the data structure
        :param element: An element to be added
        :return: self
        :rtype: MinHeap
        """
        # TODO Initialize new node

        # TODO Find insertion point and insertion point parent

        # TODO Add new node to bottom left most location

        # TODO Increment size
        pass

    def remove(self):
        """
        Remove and return the smallest element in the data structure
        :return: self
        :rtype: MinHeap
        """
        # TODO Remove old_root

        # TODO Find replacement node and replacement node parent

        # TODO Remove replacement node from tree

        # TODO Insert replacement node at root

        # TODO Move replacement node down until min heap quality satisfied

        # TODO Decrement size

        # TODO Return old_root

        pass

    def peak(self):
        """
        Return the smallest element in the data structure
        :return: The smallest element in the data structure
        """
        # TODO If root is None, return None

        # TODO If root is not None, return root value
        pass


