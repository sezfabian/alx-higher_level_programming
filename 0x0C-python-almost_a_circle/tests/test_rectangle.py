#!/usr/bin/python3
"""Rectangle class test module"""

import unittest
import sys
import io
import unittest.mock
from models.base import Base
from models.rectangle import Rectangle


class Test_Rctangle(unittest.TestCase):
    """Rectangle Test Class"""

    def test_id_rect(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(12, 4)
        self.assertEqual(r2.id, r1.id + 1)

    def test_id_rect_unique(self):
        r1 = Rectangle(2, 10, 0, 0, 12)
        self.assertEqual(r1.id, 12)

    def test_id_rect_base_combined(self):
        r1 = Base()
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, r1.id + 1)

    def test_empty_init(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_one_arg_init(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10)

    def test_6_arg_init(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 3, 4, 5, 6)

    def test_5int_arg_init(self):
        r1 = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 5)

    def test_init_rect_2_args(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_rect_init_width_str(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle("str", 2)

    def test_rect_init_width_float(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(5.5, 2)

    def test_rect_init_width_0(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)

    def test_rect_init_width_negative(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)

    def test_rect_init_height_str(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, "str")

    def test_rect_init_height_float(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 5.5)

    def test_rect_init_height_0(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(2, 0)

    def test_rect_init_height_negative(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(2, -2)

    def test_rect_x(self):
        r1 = Rectangle(2, 10)
        r2 = Rectangle(2, 10, 1)
        r3 = Rectangle(2, 10, 1, 2)
        r4 = Rectangle(2, 10, 1, 2, 13)
        self.assertEqual(r1.x, 0)
        self. assertEqual(r2.x, r3.x, 1)
        self.assertEqual(r4.x, 1)

    def test_rect_y(self):
        r1 = Rectangle(2, 10)
        r2 = Rectangle(2, 10, 1)
        r3 = Rectangle(2, 10, 1, 2)
        r4 = Rectangle(2, 10, 1, 2, 13)
        self.assertEqual(r1.y, r2.y, 0)
        self.assertEqual(r3.y, r4.y, 2)

    def test_rect_x_str(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 10, "str", 2)

    def test_rect_y_str(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 10, 2, "str")

    def test_rect_x_negative(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(2, 10, -2, 2)

    def test_rect_y_negative(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(2, 10, 2, -2)

    def test_rect_x_0(self):
        r1 = Rectangle(2, 10, 0, 2)
        self.assertEqual(r1.x, 0)

    def test_rect_y_0(self):
        r1 = Rectangle(2, 10, 0, 0)
        self.assertEqual(r1.y, 0)

    def test_rect_x_float(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 10, 0.8, 0)

    def test_rect_y_float(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 10, 0, 0.5)

    def test_rect_setter(self):
        r1 = Rectangle(2, 6, 1, 1, 7)
        r1.width = 4
        r1.height = 4
        r1.x = 2
        r1.y = 2
        self.assertEqual(r1.width, r1.height, 4)
        self.assertEqual(r1.x, r1.y, 2)

    def test_rect_area(self):
        r1 = Rectangle(2, 10)
        self.assertEqual(r1.area(), 20)

    def test_area_one_arg(self):
        r1 = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r1.area(1)
        with self.assertRaises(TypeError):
            Rectangle.area(1, 1)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_rect_display(self, mock_stdout):
        r1 = Rectangle(4, 5)
        r1.display()
        self.assertEqual(mock_stdout.getvalue(), "####\n####\n####\n####\n####\n")

    def test_rect_display_arg(self):
        r1 = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            r1.display(1)

    def test_rect_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_rect_displaypro(self, mock_stdout):
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        self.assertEqual(mock_stdout.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_rect_update1(self):
        r0 = Rectangle(8, 8)
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] ({}) 10/10 - 10/10".format(r0.id + 1))

    def test_rect_update2(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

    def test_rect_update3(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

    def test_rect_update4(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

    def test_rect_update5(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

    def test_rect_update6(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

