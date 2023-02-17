#!/usr/bin/python3
"""Test Square Module"""
import unittest
import unittest
import sys
import io
import unittest.mock
import json
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """TestSquare Class"""

    def test_Square_id(self):
        r0 = Square(1)
        r1 = Square(2)
        r2 = Square(4, 5)
        r3 = Square(6, 4, 2)
        r4 = Square(3, 5, 6, 7)
        self.assertEqual(r1.id, r0.id + 1)
        self.assertEqual(r2.id, r1.id + 1)
        self.assertEqual(r3.id, r2.id + 1)
        self.assertEqual(r4.id, 7)

    def test_square_id_none(self):
        r3 = Square(1)
        r4 = Square(5, 5, 6, None)
        self.assertEqual(r4.id, r3.id + 1)

    def test_square_x(self):
        r1 = Square(5)
        r2 = Square(7, 5)
        r3 = Square(6, 9, 2)
        r4 = Square(2, 9, 6, 7)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r3.x, 9)
        self.assertEqual(r4.x, 9)

    def test_square_no_arg(self):
        with self.assertRaises(TypeError):
            r1 = Square()

    def test_square_0size(self):
        with self.assertRaises(ValueError):
            r1 = Square(0)

    def test_square_size_str(self):
        with self.assertRaises(TypeError):
            r1 = Square("str")

    def test_square_size_float(self):
        with self.assertRaises(TypeError):
            r1 = Square(1.6)

    def test_square_size_list(self):
        with self.assertRaises(TypeError):
            r1 = Square([1, 2, 3])

    def test_square_size_bool(self):
        with self.assertRaises(ValueError):
            s1 = Square(False)

    def test_square_size_tuple(self):
        with self.assertRaises(TypeError):
            s1 = Square({1, 2})

    def test_square_size_private(self):
        s1 = Square(2, 3)
        self.assertEqual(hasattr(s1, "__size"), False)
        self.assertEqual(hasattr(s1, "_Rectangle__width"), True)
        self.assertEqual(hasattr(s1, "_Rectangle__height"), True)

    def test_square_x_private(self):
        s1 = Square(2, 3)
        self.assertEqual(hasattr(s1, "__x"), False)
        self.assertEqual(hasattr(s1, "_Rectangle__x"), True)

    def test_square_six_args_instance(self):
        with self.assertRaises(TypeError):
            s = Square(1, 1, 1, 1, 1, 1)

    def test_square_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, "wed")

    def test_square_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, 5.6)

    def test_square_y_float(self):
        def test_square_x_float(self):
            with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Square(10, 3, 5.6)

    def test_square_update(self):
        s0 = Square(8)
        s1 = Square(10, 10, 10)
        self.assertEqual("[Square] ({}) 10/10 - 10".format(s0.id + 1), str(s1))

    def test_square_area(self):
        s1 = Square(10, 10, 10)
        self.assertEqual(s1.area(), 100)

    def test_square_str(self):
        s1 = Square(5, 0, 0, 5)
        self.assertEqual(str(s1), "[Square] (5) 0/0 - 5")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_square_display(self, mock_stdout):
        s1 = Square(5)
        s1.display()
        self.assertEqual(mock_stdout.getvalue(), \
            "#####\n#####\n#####\n#####\n#####\n")

    def test_to_dictionary(self):
        s1 = Square(10, 5, 6, 7)
        d1 = {'id': 7, 'x': 5, 'size': 10, 'y': 6}
        self.assertEqual(s1.to_dictionary(), d1)

    def test_square_to_dictionary_arg(self):
        s1 = Square(10, 5, 6, 7)
        d1 = {'id': 7, 'x': 5, 'size': 10, 'y': 6}
        with self.assertRaises(TypeError):
            self.assertEqual(s1.to_dictionary(1), d1)

    def test_square_to_dictionary_two_instance(self):
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        self.assertEqual(s1 == s2, False)

    def test_to_json_string_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(10)
        d1 = s1.to_dictionary()
        d2 = s2.to_dictionary()
        json_string = Base.to_json_string([d1, d2])
        squares = json.loads(json_string)
        self.assertDictEqual(d1, squares[0])
        self.assertDictEqual(d2, squares[1])

    def test_create_square(self):
        dict = {'x': 1, 'size': 3, 'id': 3, 'y': 0}
        r1 = Square.create(**dict)
        self.assertEqual(str(r1), "[Square] (3) 1/0 - 3")

    def test_create_square1(self):
        r1 = Square(3, 5, 1, 3)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Square] (3) 5/1 - 3")
        self.assertEqual(str(r2), "[Square] (3) 5/1 - 3")
        self.assertEqual((r1 is r2), False)

    def test_create_square1(self):
        r1 = Square(3, 5, 1, 3)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Square] (3) 5/1 - 3")
        self.assertEqual(str(r2), "[Square] (3) 5/1 - 3")
        self.assertEqual((r1 is r2), False)

    def test_load_from_file_square(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        squares = [s1, s2]
        Square.save_to_file(squares)
        squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(squares_output[0]))
        self.assertEqual(str(s2), str(squares_output[1]))
        self.assertIsNot(s1, squares_output[0])
        self.assertIsNot(s2, squares_output[1])
        self.assertNotEqual(s1, squares_output[0])
        self.assertNotEqual(s2, squares_output[1])
