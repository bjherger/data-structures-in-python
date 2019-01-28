import logging
from functools import total_ordering


class Queue(object):
    """
    A queue implementation, with the following attributes

     - First in, first out

    """

    def __init__(self):
        self.head = QueueNode(None)
        self.head.isHead = True
        self.size = 0

    def add(self, element):
        """
        Add the element to the data structure
        :param element: An element to be added
        :return: self
        :rtype: Queue
        """
        # Create newNode
        new_node = QueueNode(element)

        # Find end
        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next

        # Add to end
        pointer.next = new_node

        # Increment size
        self.size += 1

        # Return self
        return self

    def remove(self):
        """
        Remove the element from the head of the data structure, or None if there is no data in the data structure
        :return: element data or None
        """
        # TODO Initialize pointer
        pointer = self.head

        # If no first node, return None
        if pointer.next is None:
            return None

        # If first node, remove from data structure and return that node
        else:
            return_node = pointer.next
            pointer.next = return_node.next

            # Decrement size
            self.size -=1
            return return_node.data

    def peak(self):
        """
        Return the value of head of the data structure
        :return: Element at the head of the list.
        """
        if self.head.next is None:
            return None
        else:
            return self.head.next.data


    def contains(self, query_element):
        """
        Determine if the query element is in the linked list
        :param query_element: An element to check for in the data structure
        :return: A boolean, indicating whether the query element occurs in the data structure at least once
        :rtype: bool
        """
        pointer = self.head.next

        while pointer is not None:
            if pointer.data == query_element:
                return True
            pointer = pointer.next
        return False


class QueueNode(object):

    def __init__(self, data):
        self.isHead = False
        self.data = data
        self.next = None
