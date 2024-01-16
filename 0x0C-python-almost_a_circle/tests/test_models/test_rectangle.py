#!/usr/bin/python3
"""unittest of rectangle module"""

import unittest
import pep8
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """testing methods and attributes of the class."""

    def test_rectangle_instantiation(self):
        """testing initialization of Rectangle class"""
        r1 = Rectangle(11, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 11)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.width, 11)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(4, 27, 37, 81)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r2.height, 27)
        self.assertEqual(r2.x, 37)
        self.assertEqual(r2.y, 81)
        r3 = Rectangle(23, 88, 45, 15, 72)
        self.assertEqual(r3.id, 72)
        self.assertEqual(r3.width, 23)
        self.assertEqual(r3.height, 88)
        self.assertEqual(r3.x, 45)
        self.assertEqual(r3.y, 15)


    def test_pep8(self):
        """test that code follows pep8 style"""
        pep8style = pep8.styleGuide(quite=True)
        result = pep8style.check_files(['models/base.py',
                                        'models/rectangle.py',
                                        'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
