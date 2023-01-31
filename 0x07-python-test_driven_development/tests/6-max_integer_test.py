#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ max_integer unittest"""
    def test_max_integer(self):
        """ test_max_integer function """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([2, 4, 1, 3]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([-3, -2, -1, 0]), 0)
        self.assertEqual(max_integer([1.0, 2, 3.3, 4]), 4)
        self.assertEqual(max_integer([1.0, 2, 3.3, 4.5]), 4.5)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer("Error"), "r")
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_types(self):
        """ test_types function """
        self.assertRaises(TypeError, max_integer, 4)
        self.assertRaises(TypeError, max_integer, {1, 2, 3, 4})
        self.assertRaises(TypeError, max_integer, ["1", 2, 3, 4])
        self.assertRaises(TypeError, max_integer, True)

if __name__ == '__main__':
    unittest.main()
