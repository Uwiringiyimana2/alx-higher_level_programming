#!/usr/bin/python3
"""unittest for Base class"""


import unittest
# import pep8
from models.base import Base


class TestBase(unittest.TestCase):
    """testing functions for Base class"""

    def test_base_instantiation(self):
        """test initiatization of id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 73)
        b4 = Base()
        self.assertEqual(b4.id, 3)
"""
    def test_pep8(self):
       # test that code follows pep8 style
        pep8style = pep.styleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
            'models/rectangle.py',
            'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                "Found code style errors (and warnings).")
"""
