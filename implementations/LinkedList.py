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
        self.head = LinkedListNode(None)
        self.head.isHead = True
        self.size = 0

    def add(self, element):
        """
        Add the element to the end of the list
        :param element: An element to be added
        :return: self
        :rtype: LinkedList
        """
        # TODO Create new node
        # TODO Find End of list
        # TODO Add new node to end of list
        # TODO Increment size
        pass

    def remove(self):
        """
        Remove the element from the head of the list
        :return: element, or None if no elements
        """
        # TODO Find end of list
        # TODO Remove end of list
        # TODO Return end of list
        pass

    def peak(self):
        """
        Return the value of the head of the list, without removing it from the list
        :return: Element at the head of the list.
        """
        # TODO Find end of list
        # TODO Return end of list
        pass

    def contains(self, query_element):
        """
        Determine if the query element is in the linked list
        :param query_element: An element to check for in the data structure
        :return: A boolean, indicating whether the query element occurs in the data structure at least once
        :rtype: bool
        """
        # TODO Iterate through LinkedList until element is found or we hit the end
        # TODO Return True if element found
        # TODO Return False if we hit the end of the list
        pass

    def size(self):
        """
        Returns the number of elements in the list
        :return: The number of elements in the list
        :rtype: int
        """
        return self.size


class LinkedListNode(object):
    def __init__(self, data):
        self.isHead = False
        self.data = data
        self.next = None
        pass
