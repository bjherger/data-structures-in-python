import logging
import unittest

from implementations.MinHeap import MinHeap

logging.getLogger().setLevel(logging.DEBUG)


class TestMinHeap(unittest.TestCase):

    def test_api(self):
        data_structure = MinHeap()
        required_methods = ['add', 'remove', 'peak', 'size']
        for required_method in required_methods:
            self.assertTrue(hasattr(data_structure, required_method))

    def test0(self):
        data_structure = MinHeap()
        data_structure.add(12)
        data_structure.add(6)
        data_structure.add(18)
        removed = data_structure.remove()

        self.assertEqual(6, removed)

    def test1(self):
        data_structure = MinHeap()
        data_structure.add(12)
        data_structure.add(12)
        removed = data_structure.remove()

        self.assertEqual(12, removed)

    def test2(self):
        data_structure = MinHeap()
        data_structure.add(17)
        removed = data_structure.remove()
        self.assertEqual(17, removed)


    def test3(self):
        data_structure = MinHeap()
        removed = data_structure.remove()
        self.assertEqual(None, removed)

        data_structure.add(17)

        data_structure.add(19)
        data_structure.add(23)

        removed = data_structure.remove()
        self.assertEqual(17, removed)

    def test4(self):
        data_structure = MinHeap()

        sample_data = [124, 123, 451351, -234, 124, 351235, 51235, 51325, 3523512351235, -213512351]
        sample_data_sorted = sorted(sample_data)
        for sample_element in sample_data:
            data_structure.add(sample_element)

        self.assertEqual(len(sample_data), data_structure.size)

        for sample_element in sample_data_sorted:

            removed = data_structure.remove()
            self.assertEqual(sample_element, removed)
