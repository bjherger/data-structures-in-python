import logging
from functools import total_ordering


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
        self.root = None

    def add(self, element):
        """
        Add a new node, containing the element, to the tree
        :param element: An item to be added to the tree
        :return: self
        :rtype: BinarySearchTree
        """
        # Create new node
        new_node = BinaryNode(element)

        # Initialize pointer with root
        pointer = self.root

        # If root is empty, new node becomes root
        if pointer is None:
            logging.debug('No existing root. New node {} becomes root'.format(new_node))

            # Insert the new element
            self.root = new_node

        # Otherwise iterate through tree until we've found the appropriate place for the new node
        else:
            next_pointer = pointer.left if pointer > new_node else pointer.right
            logging.debug('pointer: {}. next_pointer: {}'.format(pointer, next_pointer))
            while next_pointer is not None:
                pointer = next_pointer
                next_pointer = pointer.left if new_node <= pointer else pointer.right
                logging.debug('pointer: {}. next_pointer: {}'.format(pointer, next_pointer))

            if new_node <= pointer:
                logging.debug('Adding new_node: {} as left to existing tree, with parent: {}'.format(new_node, pointer))
                pointer.left = new_node
            else:
                logging.debug('Adding new_node: {} as right to existing tree, with parent: {}'.format(new_node,
                                                                                                      pointer))
                pointer.right = new_node

        # Return self
        return self

    def contains(self, query_element):
        """
        Determine if an item equal to the query_element is contained in the tree
        :param query_element: An item to be compared to tree contents
        :return: A boolean, indicating if the tree contains an element equal to the query_element
        """
        logging.debug('Checking if data_structure contains: {}'.format(query_element))
        # Initialize query node
        query_node = BinaryNode(query_element)

        # Initialize pointer with root
        pointer = self.root
        logging.debug('pointer: {}.'.format(pointer))

        # If root is empty, query_element cannot be in the tree
        if pointer is None:
            return False
        logging.debug('pointer: {}. pointer children: {} {}'.format(pointer, pointer.left, pointer.right))
        # Move through tree
        while pointer is not None:
            logging.debug('pointer: {}. pointer children: {} {}'.format(pointer, pointer.left, pointer.right))
            if pointer == query_node:
                logging.debug('pointer found')
                return True
            else:
                pointer = pointer.left if query_node <= pointer else pointer.right
        return False

    def remove(self, query_element):
        """
        Remove an element equivalent to the element, if there is one. Throw a ValueError if the element is not
        contained in the tree
        :param query_element: An item to be removed from the tree
        :return: self
        :rtype: BinarySearchTree
        """
        logging.debug('Attempting to remove query_element: {}'.format(query_element))
        # TODO Return error if there is no root
        # TODO Pass data to remove_helper
        pass


    def remove_helper(self, query_node, pointer):
       # TODO Locate match node and match_node_parent
       # TODO Determine match node replacement
       # TODO Remove match node replacement, if necessary
       # TODO Replace match node with match node replacement
       pass

    def find_smallest_right_descendant(self, pointer):
        # TODO If pointer has no children, return None
        # TODO If match node has one child, return that child
        # TODO If match node has two children, return smallest right.
        pass

    def in_order_traversal(self):
        """
        Traverse the tree in order. This returns a sorted list of tree contents. This sorting is not stable (equal
        elements will be returned in an arbitrary order)
        :return: A list containing sorted tree elements
        :rtype: list
        """
        if self.root is None:
            return []
        else:
            return self.in_order_traversal_helper(self.root)
        pass

    def in_order_traversal_helper(self, node):
        # Base case: No children
        if node is None:
            return []
        # Return left traversal, self, right traversal
        return self.in_order_traversal_helper(node.left) + [node.data] + self.in_order_traversal_helper(node.right)


@total_ordering
class BinaryNode(object):
    """
    A binary node, with a left child, right child and some data
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def remove_left(self):
        left = self.left
        self.left = None
        return left

    def remove_right(self):
        right = self.right
        self.right = None
        return right

    def _is_valid_operand(self, other):
        return isinstance(other, BinaryNode)

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.data == other.data

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.data < other.data

    def __str__(self):
        return str('<Node {}>'.format(self.data))
