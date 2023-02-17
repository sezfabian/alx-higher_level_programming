#!/usr/bin/python3
"""Rectangle class test module"""

import unittest
import sys
import io
import unittest.mock
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_rect_update7(self):
        r1 = Rectangle(10, 10, 10, 10, 5)
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (5) 10/10 - 10/1")

    def test_rect_update8(self):
        r1 = Rectangle(10, 10, 10, 10, 5)
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (5) 2/10 - 1/10")

    def test_rect_update9(self):
        r1 = Rectangle(10, 10, 10, 10, 5)
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/10")

    def test_rect_update10(self):
        r1 = Rectangle(10, 10, 10, 10, 89)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_rect_update11(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10, 10, 10, 89)
            r1.update(1, 2, 3, 4, 5, 6, 7, 8)

    def test_to_dictionary1(self):
        r1 = Rectangle(3, 5, 6, 7, 14)
        d1 = {"x": 6, "y": 7, "id": 14, "height": 5, "width": 3}
        with self.assertRaises(TypeError):
            self.assertEqual(r1.to_dictionary(1), d1)

    def test_to_dictionary(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(3, 5, 6, 7)
        d1 = {"x": 0, "y": 0, "id": r2.id - 1, "height": 3, "width": 2}
        d2 = {"x": 6, "y": 7, "id": r1.id + 1, "height": 5, "width": 3,}
        self.assertEqual(r1.to_dictionary(), d1)
        self.assertEqual(r2.to_dictionary(), d2)

    def test_to_dictionary_arg(self):
        r1 = Rectangle(3, 5, 6, 7)
        with self.assertRaises(TypeError):
            d1 = r1.to_dictionary(2)

    def test_to_json_string_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(10, 7, 2)
        d1 = r1.to_dictionary()
        d2 = r2.to_dictionary()
        json_string = Base.to_json_string([d1, d2])
        rectangles = json.loads(json_string)
        self.assertDictEqual(d1, rectangles[0])
        self.assertDictEqual(d2, rectangles[1])

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_from_json_to_string_empty(self):
        json_list_input = Rectangle.to_json_string(None)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(None, list_output)

    def test_from_json_to_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_create_rect(self):
        dict = {'x': 1, 'width': 3, 'id': 3, 'height': 5, 'y': 0}
        r1 = Rectangle.create(**dict)
        self.assertEqual(str(r1), "[Rectangle] (3) 1/0 - 3/5")

    def test_create_rect1(self):
        r1 = Rectangle(3, 5, 1, 0, 3)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (3) 1/0 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (3) 1/0 - 3/5")
        self.assertEqual((r1 is r2), False)

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))
        self.assertIsNot(r1, list_rectangles_output[0])
        self.assertIsNot(r2, list_rectangles_output[1])
        self.assertNotEqual(r1, list_rectangles_output[0])
        self.assertNotEqual(r2, list_rectangles_output[1])


    def test_load_from_file_type(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(type(list_rectangles_output), list)
        areRect = all(type(o) is Rectangle for o in list_rectangles_output)
        self.assertEqual(areRect, True)

    def load_from_file_two_times_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_r1 = Rectangle.load_from_file()
        list_r2 = Rectangle.load_from_file()
        self.assertEqual(list_r1, list_r2)
        self.assertIsNot(list_r1, list_r2)

    def test_load_from_file_no_file(self):
        if os.path.isfile("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.isfile("Square.json"):
            os.remove("Square.json")
        r = Rectangle.load_from_file()
        self.assertEqual(r, [])
        s = Square.load_from_file()
        self.assertEqual(s, [])
