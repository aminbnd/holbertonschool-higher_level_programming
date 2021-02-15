#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ unittest class for max_integer function """
    
    def test_module_docstr(self):
        """ Test module docstring """
        mod = __import__('6-max_integer').__doc__
        self.assertTrue(len(mod) > 1)
    
    def test_func_docstr(self):
        """ Test function docstring """
        func = max_integer.__doc__
        self.assertTrue(len(func) > 1)
    
    def test_void_list(self):
        """ Test for empty list """
        lst = []
        self.assertIsNone(max_integer(lst))
    
    def test_one_number_list(self):
        """ Test for one item list """
        lst = [98]
        self.assertEqual(max_integer(lst), 98)
    
    def test_begin(self):
        """ Test if the maximum is in the begining of the list """
        lst = [98, 1, 2]
        self.assertEqual(max_integer(lst), 98)
    
    def test_middle(self):
        """ Tests if the maximum is in the middle of the list """
        lst = [1, 98, 5]
        self.assertEqual(max_integer(lst), 98)

    def test_end(self):
        """ Tests if the maximum is in the end of the list """
        lst = [1, 5, 98]
        self.assertEqual(max_integer(lst), 98)

    def test_negative(self):
        """ Test for list containing only negative numbers """
        lst = [-1, -5, -98]
        self.assertEqual(max_integer(lst), -1)

    def one_negative(self):
        """ Tests for a list containing one negative number """
        lst = [1, 5, -98]
        self.assertEqual(max_integer())

    def one_positive(self):
        """ Test for a list containing one positive number """
        lst = [-1, -5, 98]
        self.assertEqual(max_integer(lst), 98)
    
    def equal_pos_numbers(self):
        """ Test for a list containing equal positive numbers """
        lst = [98, 98, 98]
        self.assertEqual(max_integer(lst), 98)
    
    def equal_neg_numbers(self):
        """ Test for a list containing equal negative numbers """
        lst = [-98, -98, -98]
        self.assertEqual(max_integer(lst), -98)
    
    if __name__ == "__main__":
        unittest.main()
