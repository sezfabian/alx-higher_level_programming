#!/usr/bin/python3
"""Base class test module"""


import unittest
import json
from models.base import Base
class TestBase(unittest.TestCase):
    """Base tests class"""

    def test_id_no_arg_twice(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id+1)

    def test_id_int_arg(self):
        b3 = Base(7)
        self.assertEqual(b3.id, 7)

    def test_id_int_arg_used(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(9)
        self.assertEqual(b3.id, 9)

    def test_id_after_arg_used(self):
        b1 = Base()
        b2 = Base(9)
        b3 = Base()
        self.assertEqual(b3.id, b1.id+1)

    def test_id_float_arg_used(self):
        b1 = Base(5.5)
        self.assertEqual(b1.id, 5.5)

    def test_id_public(self):
        b1 = Base(9)
        b1.id = 15
        self.assertEqual(15, b1.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            b1 = Base(9)
            print(b1.__nb_instances)

    def test_id_same_arg(self):
        b1 = Base(9)
        b2 = Base(9)
        self.assertEqual(b1.id, b2.id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            b1 = Base(2, 9)

    def test_string_arg(self):
        b1 = Base("str")
        self.assertEqual(b1.id, "str")

    def test_none_arg(self):
        b1 = Base()
        b2 = Base(None)
        self.assertEqual(b2.id , b1.id + 1)

    def test_negative_arg(self):
        b1 = Base(-9)
        self.assertEqual(b1.id, -9)

    def test_undefined_arg(self):
        with self.assertRaises(NameError):
            b1 = Base(nonid)

    def test_id_char_arg(self):
        b1 = Base("i")
        self.assertEqual(b1.id, "i")

    def test_complex_id(self):
        b1 = Base(2 + 1j)
        self.assertEqual(b1.id, 2 + 1j)

    def test_id_list_arg(self):
        b1 = Base([1, 2, 3])
        self.assertEqual(b1.id, [1, 2, 3])

    def test_id_tuple_arg(self):
        b1 = Base({1, 2, 3})
        self.assertEqual(b1.id, {1, 2, 3})

    def test_id_number_of_objects(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(Base._Base__nb_objects, 8)

    def test_to_json_string_simple(self):
        json_string = Base.to_json_string([{"id": 1}])
        self.assertEqual(json_string, '[{"id": 1}]')

    def test_to_json_string(self):
        dict = []
        dict.append({'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        dict.append({'x': 2, 'width': 12, 'id': 2, 'height': 10, 'y': 8})
        json_string = Base.to_json_string(dict)
        dict_from_json = json.loads(json_string)
        self.assertEqual(type(dict_from_json), list)
        self.assertEqual(dict_from_json, dict)

    def test_to_json_string_two_times(self):
        dict = []
        dict.append({'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        dict.append({'x': 2, 'width': 12, 'id': 2, 'height': 10, 'y': 8})
        json_string1 = Base.to_json_string(dict)
        json_string2 = Base.to_json_string(dict)
        self.assertEqual(json_string1, json_string2)

    def test_to_json_string_empty(self):
        json_string = Base.to_json_string([])
        self.assertEqual(type(json_string), str)
        self.assertEqual(json_string, "[]")
