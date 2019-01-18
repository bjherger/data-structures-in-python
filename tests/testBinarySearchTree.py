import logging
import unittest

from implementations.BinarySearchTree import BinarySearchTree

logging.getLogger().setLevel(logging.DEBUG)

class TestBinarySearchTree(unittest.TestCase):

    def test_api(self):
        data_structure = BinarySearchTree()
        required_methods = ['add', 'contains', 'remove', 'in_order_traversal']
        for required_method in required_methods:
            self.assertTrue(hasattr(data_structure, required_method))

    def test0(self):
        data_structure = BinarySearchTree()
        data_structure.add(12)
        data_structure.add(6)
        data_structure.add(18)
        data_structure.remove(12)

        self.assertTrue(data_structure.contains(6))
        self.assertTrue(data_structure.contains(18))
        self.assertFalse(data_structure.contains(12))

        self.assertListEqual([6, 18], data_structure.in_order_traversal())

    def test1(self):
        data_structure = BinarySearchTree()
        data_structure.add(12)
        data_structure.add(12)
        data_structure.remove(12)

        self.assertTrue(data_structure.contains(12))
        self.assertListEqual([12], data_structure.in_order_traversal())


    def test2(self):
        data_structure = BinarySearchTree()
        data_structure.add(17)
        self.assertTrue(data_structure.contains(17))

    def test3(self):
        data_structure = BinarySearchTree()
        self.assertFalse(data_structure.contains(17))
        data_structure.add(17)
        self.assertTrue(data_structure.contains(17))

        data_structure.add(19)
        data_structure.add(23)
        self.assertTrue(data_structure.contains(17))
        self.assertTrue(data_structure.contains(19))
        self.assertTrue(data_structure.contains(23))

        data_structure.remove(23)
        self.assertFalse(data_structure.contains(23))
        self.assertTrue(data_structure.contains(17))
        self.assertTrue(data_structure.contains(19))
        pass

    def test4(self):
        data_structure = BinarySearchTree()

        sample_data = [124, 123, 451351, -234, 124, 351235, 51235, 51325, 3523512351235, -213512351]
        sample_data_sorted = sorted(sample_data)

        for sample_element in sample_data:
            data_structure.add(sample_element)

        in_order_traversal = data_structure.in_order_traversal()
        self.assertListEqual(sample_data_sorted, in_order_traversal)
        pass

    def test5(self):
        data_structure = BinarySearchTree()

        data_structure.add(15)
        data_structure.remove(15)
        data_structure.add(15)
        data_structure.add(15)
        data_structure.remove(15)
        data_structure.add(23)
        data_structure.add(92)
        data_structure.add(-1)
        data_structure.add(-12)
        data_structure.remove(23)

        expected_result = sorted([15, 92, -1, -12])
        in_order_traversal = data_structure.in_order_traversal()
        self.assertListEqual(expected_result, in_order_traversal)

        self.assertRaises(ValueError, data_structure.remove, 42)
