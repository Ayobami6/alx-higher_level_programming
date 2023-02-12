#!/usr/bin/python3

import os
import unittest
from models.base import Base


class TestBase_1st(unittest.TestCase):

    def test_no_param_1_instance(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_no_param_3_instances(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 3)
