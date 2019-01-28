import logging
from functools import total_ordering


class MinHeap(object):
    """
    A min heap implementation, with the following attributes

     - Complete tree
     - Root is minimum of all values
     - Parents are always less than (or equal to) children

    """

    def __init__(self):
        self.array = list()

    def add(self, element):
        """
        Add the element to the data structure
        :param element: An element to be added
        :return: self
        :rtype: MinHeap
        """
        # Add element to list
        self.array.append(element)
        new_element_index = len(self.array) - 1
        parent_index = new_element_index // 2

        # Sieve up until min heap quality satisfied
        while (parent_index >= 0) and (self.array[new_element_index] < self.array[parent_index]):
            tmp = self.array[new_element_index]
            self.array[new_element_index] = self.array[parent_index]
            self.array[parent_index] = tmp
            new_element_index = parent_index
            parent_index = new_element_index // 2

        pass

    def remove(self):
        """
        Remove and return the smallest element in the data structure
        :return: self
        :rtype: MinHeap
        """

        # TODO If nothing to remove, return None
        if len(self.array) <= 0:
            return None

        # Remove return_value
        return_value = self.array[0]

        # Find replacement_value
        replacement_value = self.array[-1]

        # Remove replacement element
        self.array = self.array[:-1]

        # Insert replacement element at root
        if len(self.array) > 1:
            self.array[0] = replacement_value
        else:
            self.array = [replacement_value]

        # Sieve down replacement element down until min heap quality satisfied
        replacement_index = 0

        while True:
            left_index = replacement_index * 2
            right_index = replacement_index * 2 + 1
            max_index = len(self.array) - 1

            # If no children, no swap necessary
            if max_index < left_index:
                break

            # If only left child, check if swap necessary
            if max_index < right_index:

                if self.array[left_index] < self.array[replacement_index]:
                    tmp = self.array[left_index]
                    self.array[left_index] = self.array[replacement_index]
                    self.array[replacement_index] = tmp

                    replacement_index = left_index
                else:
                    break

            # If two children, find if swap necessary w/ smaller child
            else:
                switch_index = right_index if self.array[right_index] < self.array[left_index] else left_index

                if self.array[switch_index] < self.array[replacement_index]:
                    tmp = self.array[switch_index]
                    self.array[switch_index] = self.array[replacement_index]
                    self.array[replacement_index] = tmp

                    replacement_index = switch_index
                else:
                    break

        # Return old_root
        return return_value

    def peak(self):
        """
        Return the smallest element in the data structure
        :return: The smallest element in the data structure
        """
        # If no data, return None
        if len(self.array) <= 0:
            return None

        # If root is not None, return root value
        else:
            return self.array[0]
