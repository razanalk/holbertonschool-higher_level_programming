#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test list with one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_integers(self):
        """Test positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        """Test max value in middle"""
        self.assertEqual(max_integer([1, 8, 3, 4]), 8)

    def test_negative_integers(self):
        """Test negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test mixed positive and negative integers"""
        self.assertEqual(max_integer([-5, 10, 3, -1]), 10)

    def test_float_numbers(self):
        """Test float values"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_string(self):
        """Test string input"""
        self.assertEqual(max_integer("Brennon"), "r")


if __name__ == "__main__":
    unittest.main()
