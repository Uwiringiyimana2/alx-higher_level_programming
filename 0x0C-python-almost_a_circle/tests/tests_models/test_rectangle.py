#!/usr/bin/python3
"""unittest of rectangle module"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_validate(self):
        self.assertRaises(TypeError, Rectangle(10, "2"))
        self.assertRaises(TypeError, Rectangle, -10)
        self.assertRaises(TypeError, Rectangle(2, -2, "2", -4)
