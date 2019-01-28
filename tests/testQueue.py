import logging
import unittest

from implementations.Queue import Queue

logging.getLogger().setLevel(logging.DEBUG)


class TestQueue(unittest.TestCase):

    def test_api(self):
        data_structure = Queue()
        required_methods = ['add', 'remove', 'peak', 'contains', 'size']
        for required_method in required_methods:
            self.assertTrue(hasattr(data_structure, required_method))

    def test0(self):
        data_structure = Queue()
        data_structure.add(12)
        data_structure.add(6)
        data_structure.add(18)
        removed = data_structure.remove()

        self.assertTrue(data_structure.contains(6))
        self.assertTrue(data_structure.contains(18))
        self.assertFalse(data_structure.contains(12))
        self.assertEqual(12, removed)

    def test1(self):
        data_structure = Queue()
        data_structure.add(12)
        data_structure.add(12)
        removed = data_structure.remove()

        self.assertTrue(data_structure.contains(12))
        self.assertEqual(12, removed)

    def test2(self):
        data_structure = Queue()
        data_structure.add(17)
        self.assertTrue(data_structure.contains(17))

    def test3(self):
        data_structure = Queue()
        self.assertFalse(data_structure.contains(17))
        data_structure.add(17)
        self.assertTrue(data_structure.contains(17))

        data_structure.add(19)
        data_structure.add(23)
        self.assertTrue(data_structure.contains(17))
        self.assertTrue(data_structure.contains(19))
        self.assertTrue(data_structure.contains(23))

        removed = data_structure.remove()
        self.assertEqual(17, removed)
        self.assertTrue(data_structure.contains(19))
        self.assertTrue(data_structure.contains(23))
        self.assertFalse(data_structure.contains(17))

    def test4(self):
        data_structure = Queue()

        sample_data = [124, 123, 451351, -234, 124, 351235, 51235, 51325, 3523512351235, -213512351]
        sample_data_sorted = sorted(sample_data)
        for sample_element in sample_data:
            data_structure.add(sample_element)

        self.assertEqual(len(sample_data), data_structure.size)

        for sample_element in sample_data_sorted:
            self.assertTrue(data_structure.contains(sample_element))

        for sample_element in sample_data:
            self.assertTrue(data_structure.contains(sample_element))

            removed = data_structure.remove()
            self.assertEqual(sample_element, removed)
