#!/usr/bin/python3
""" Rectangle test module
"""

import os
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle_1st(unittest.TestCase):
    def setUp(self):
        print("Testing Rectangle")

    def test_width(self):
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.width, 4)

    def test_height(self):
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.height, 5)

    def test_no_param(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle()

    def test_1_param(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle(3)

    def test_rect_from_base(self):
        self.assertIsInstance(Rectangle(4, 5), Base)


if __name__ == "__main__":
    unittest.main()
