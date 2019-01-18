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
        # Create new node
        new_node = LinkedListNode(element)
        # Find End of list
        tail = self.head
        while tail.next is not None:
            tail = tail.next

        # Add new node to end of list
        tail.next = new_node

        # Increment size
        self.size +=1
        return self

    def remove(self):
        """
        Remove the element from the head of the list
        :return: element, or None if no elements
        """
        # Find top of list
        top = self.head.next

        # If no next element, return None
        if top is None:
            return None
        else:

            # Remove top of list
            self.head.next = top.next

            # Decrement size
            self.size -= 1

            # Return top of list
            return top.data

    def peak(self):
        """
        Return the value of the head of the list, without removing it from the list
        :return: Element at the head of the list, or None if no elements
        """
        # Find top of list
        top = self.head.next

        # Return top of list
        if top is not None:
            return top.data
        else:
            return None

    def contains(self, query_element):
        """
        Determine if the query element is in the linked list
        :param query_element: An element to check for in the data structure
        :return: A boolean, indicating whether the query element occurs in the data structure at least once
        :rtype: bool
        """
        # Iterate through LinkedList until element is found or we hit the end
        pointer = self.head.next

        while pointer is not None:
            # Return True if element found
            if pointer.data == query_element:
                return True

            # Move to next pointer
            pointer = pointer.next

        # Return False if we hit the end of the list
        return False


class LinkedListNode(object):
    def __init__(self, data):
        self.isHead = False
        self.data = data
        self.next = None
        pass
