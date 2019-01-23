import logging
from functools import total_ordering


class Stack(object):
    """
    A stack implementation, with the following attributes

     - First in, last out

    """

    def __init__(self):
        self.head = StackNode(None)
        self.head.isEnd = True
        self.size = 0

    def add(self, element):
        """
        Add the element to the stack
        :param element: An element to be added
        :return: self
        :rtype: Stack
        """
        # Create newNode
        new_node = StackNode(element)

        # Add existing head as next to new_node
        new_node.next = self.head

        # Update newNode to head
        self.head = new_node

        # Increment size
        self.size += 1

        # Return self
        return self

    def remove(self):
        """
        Remove the element from the head of the stack, or None if there is no data in the data structure
        :return: element data or None
        """
        return_node = self.head

        # If there is no data, return None
        if return_node.isEnd:
            return None
        else:
            self.head = return_node.next

            # Decrement size
            self.size -= 1
            return return_node.data

    def peak(self):
        """
        Return the value of head of the stack
        :return: Element at the head of the list.
        """
        return self.head.data

    def contains(self, query_element):
        """
        Determine if the query element is in the linked list
        :param query_element: An element to check for in the data structure
        :return: A boolean, indicating whether the query element occurs in the data structure at least once
        :rtype: bool
        """
        pointer = self.head

        while not pointer.isEnd:
            if pointer.data == query_element:
                return True
            pointer = pointer.next

        return False


class StackNode(object):

    def __init__(self, data):
        self.isEnd = False
        self.data = data
        self.next = None
