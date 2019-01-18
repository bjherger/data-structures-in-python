class BinarySearchTree(object):
    """
    A tree based data structure, with the following attributes:

     - Every node can have at most 2 children (left child and right child)
     - The left child must be <= the node, if there is a left child
     - The right child must be > the node, if there is a right child

    API roughly based on http://www1.cs.columbia.edu/~bert/courses/3134/slides/Lecture7.pdf
    and https://github.com/bjherger/data_structures/blob/master/bin/data_structures/binary_tree.py

    """

    def __init__(self):
        pass

    def add(self, element):
        """
        Add a new node, containing the element, to the tree
        :param element: An item to be added to the tree
        :return: self
        :rtype: BinarySearchTree
        """
        pass

    def contains(self, query_element):
        """
        Determine if an item equal to the query_element is contained in the tree
        :param query_element: An item to be compared to tree contents
        :return: A boolean, indicating if the tree contains an element equal to the query_element
        """
        pass

    def remove(self, element):
        """
        Remove an element equivalent to the element, if there is one. Throw a ValueError if the element is not
        contained in the tree
        :param element: An item to be removed from the tree
        :return: self
        :rtype: BinarySearchTree
        """
        pass

    def in_order_traversal(self):
        """
        Traverse the tree in order. This returns a sorted list of tree contents. This sorting is not stable (equal
        elements will be returned in an arbitrary order)
        :return: A list containing sorted tree elements
        :rtype: list
        """
        pass

