#!/usr/bin/python3

"""This module contains test cases for `Base` model."""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """`Base` test cases."""

    def test_ids(self):
        """It should create `Base` objects with incremental ids 1, 2, 3"""
        b = Base()
        self.assertEqual(b.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)

    def test_id_10(self):
        """It should create `Base` object with id == 10"""
        b = Base(10)
        self.assertEqual(b.id, 10)


if __name__ == "__main__":
    unittest.main()
