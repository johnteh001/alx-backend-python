#!/usr/bin/env python3
"""Task 0"""
import unittest
import json
from requests.models import Response
from unittest.mock import patch
from parameterized import parameterized
from typing import Sequence, Mapping, Any
from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """Test Class"""
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)
                           ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any):
        """Test function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)),
                           ({"a": 1}, ("a", "b"))
                           ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence):
        """Test KeyError"""
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class tests HTTP calls"""
    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})
                           ])
    def test_get_json(self, test_url: str, test_payload: Mapping):
        """Mocking get_json"""
        with patch('utils.requests') as mock_req:
            response = Response()
            if test_payload.get("payload") is True:
                response._content = b'{"payload": true}'
            else:
                response._content = b'{"payload": false}'
            mock_req.get.return_value = response
            res = get_json(test_url)
            mock_req.get.assert_called_once()
            self.assertEqual(res, test_payload)


class TestMemoize(unittest.TestCase):
    """Memoization class"""
    def test_memoize(self):
        """Test memoize method"""
        class TestClass:
            """Test class"""
            def a_method(self):
                """test method"""
                return 42

            @memoize
            def a_property(self):
                """Property of object"""
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=42) as mocked:
            test = TestClass()
            self.assertEqual(test.a_property, 42)
            self.assertEqual(test.a_property, 42)
            mocked.assert_called_once()
