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
        logging.debug('Attempting to add element: {}'.format(element))
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
        # Return error if there is no root
        if self.root is None:
            logging.debug('root is None')
            raise ValueError('Unable to remove element')
        # Pass data to remove_helper
        self.root = self.remove_helper(self.root, BinaryNode(query_element))

        # Return self
        pass

    def remove_helper(self, pointer, query_node):
        logging.debug('Attempting to remove query_node: {} from tree starting with pointer: {}'.format(query_node,
                                                                                                       pointer))
        # Locate match node and match_node_parent
        match_node_parent = None
        match_node = pointer

        logging.debug('match_node_parent: {}, match_node: {}, match_node.left: {}, match_node.right: {}'.format(
            match_node_parent, match_node, match_node.left, match_node.right))
        while match_node is not None and match_node != query_node:
            match_node_parent = match_node
            match_node = match_node.left if query_node <= match_node_parent else match_node.right
            logging.debug('match_node_parent: {}, match_node: {}'.format(match_node_parent, match_node))

        # Raise value error if query node is not in tree
        if match_node is None:
            raise ValueError('Unable to remove element')

        while match_node.left == query_node:
            logging.debug('Equal nodes. Match node to the lowest match')
            match_node_parent = match_node
            match_node = match_node.left

        logging.debug('match_node_parent: {}, match_node: {}, match_node.left: {}, match_node.right: {}'.format(
            match_node_parent, match_node, match_node.left, match_node.right))

        # Determine match node replacement
        replacement_node = self.find_replacement_node(match_node)
        logging.debug('replacement_node: {}'.format(replacement_node))

        # Remove match node replacement, if necessary
        if replacement_node is not None:
            self.remove_helper(match_node, replacement_node)
            replacement_node.left = match_node.left
            replacement_node.right = match_node.right

        # Replace match node with match node replacement
        if match_node_parent is None:
            logging.debug('replacing pointer w/ replacement_node: {}'.format(replacement_node))
            pointer = replacement_node
        elif match_node <= match_node_parent:
            match_node_parent.left = replacement_node
        else:
            match_node_parent.right = replacement_node
        logging.debug('replacement_node: {}, match_node: {}'.format(replacement_node, match_node))


        logging.debug('pointer: {}'.format(pointer))
        return pointer

    def find_replacement_node(self, pointer):
        # If pointer has no children, return None
        if pointer.left is None and pointer.right is None:
            logging.debug('No children. replacement is None')
            return None
        # If match node has one child, return that child
        elif pointer.left is None and pointer.right is not None:
            logging.debug('right child replacement')
            return pointer.right
        elif pointer.left is not None and pointer.right is None:
            logging.debug('leftchild replacement')
            return pointer.left
        # If match node has two children, return smallest right.
        else:
            logging.debug('two children')
            replacement = pointer.right
            logging.debug('replacement: {}'.format(replacement))
            while replacement.left is not None:
                replacement = replacement.left
                logging.debug('replacement: {}'.format(replacement))
            return replacement

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
        logging.debug('traversing node: {}'.format(node))
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
