#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ tests max_integer """

    def test_negative(self):
        """Test with list negative values return the max"""
        list_negative = [-2, -6, -1]
        result = max_integer(list_negative)
        self.assertEqual(result, -1)

    def test_integer(self):
        """Test with list integer values return the max"""
        list_integer = [2, 6, 1]
        result = max_integer(list_integer)
        self.assertEqual(result, 6)

    def test_max_int_basic(self):
        """ tests normal list of ints"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_list_int_empty(self):
        """ tests list empty """
        self.assertEqual(max_integer([]), None)

    def test_list_int_one(self):
        """ test list one element """
        self.assertEqual(max_integer([2]), 2)

    def test_max_beginning(self):
        """Test list return value"""
        list_beginning = [10, 8, 7, 6, 4]
        result = max_integer(list_beginning)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
