#!/usr/bin/env python3
""" Module that holds parameterize a unit test
"""

from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ [Class that inherits from unittest.TestCase]
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, mapping, path, expected):
        """ First unit test for nested_map function, (test access nested map)
            Method to test that the method returns what it is supposed to
        """
        self.assertEqual(access_nested_map(mapping, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, mapping, path):
        """ Second unit test for nested_map function,
            (test exception nested map)
            Method that use the assertRaises context manager to test
            that a KeyError is generated for some inputs
        """
        with self.assertRaises(KeyError):
            access_nested_map(mapping, path)
