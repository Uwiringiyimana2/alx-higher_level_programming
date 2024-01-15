#!/usr/bin/python3
"""unittest for Square class"""


import unittest
import pep8
from models.square import Square


class TestSquare(unittest.TestCase):
    """testing functions for Base class"""

    def test_base_instantiation(self):
        """test initiatization of id"""
        r3 = Square(24, 40, 15, 73)
        self.assertEqual(r3.id, 73)
        self.assertEqual(r3.width, 24)
        self.assertEqual(r3.height, 24)
        self.assertEqual(r3.x, 45)
        self.assertEqual(r3.y, 16)

    def test_pep8(self):
        """test that code follows pep8 style"""
        pep8style = pep.styleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'models/rectangle.py',
                                        'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
