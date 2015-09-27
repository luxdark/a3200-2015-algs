__author__ = 'erofeev'

import unittest
import radix_sort  # import radix_sort.py from current directory


class TestSorting(unittest.TestCase):
    def test_trivial(self):
        arr = [1, 333, 22]
        res = radix_sort.sort(arr)
        expected = [1, 22, 333]
        self.assertFalse(not res)  # check res not empty
        self.assertEqual(expected, res)

    def test_empty(self):
        arr = []
        res = radix_sort.sort(arr)
        expected = []
        self.assertEqual(expected, res)
