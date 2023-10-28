#!/usr/bin/env python3
"""This module showcases unit testing in Python with parameterized"""
from parameterized import parameterized
from unittest import main, TestCase
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """Unittests for utils.access_nested_map()"""
    @parameterized.expand([
        ({'a': 1}, 'a', 1),
        ({'a': {'b': 2}}, 'a', {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test parameters"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, 'a', 'a'),
        ({'a': 1}, ('a', 'b'), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, key):
        """Test raised exceptions"""
        with self.assertRaises(KeyError) as ex:
            access_nested_map(nested_map, path)
        self.assertEqual(ex.exception.args[0], key)


class TestGetJson(TestCase):
    """Unittests for utils.get_json()"""
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, MockGet):
        """Test json method response"""
        # Mock json method of requests.get response object
        response = Mock()
        response.json.return_value = test_payload
        MockGet.return_value = response

        # Test method and make sure it calls get method only once
        self.assertEqual(get_json(test_url), test_payload)
        MockGet.assert_called_once_with(test_url)


class TestMemoize(TestCase):
    """Unittests for utils.memoize()"""
    def test_memoize(self):
        """Tests memoization in the memoize function"""
        class TestClass:
            """A simple class for testing memoize"""

            def a_method(self):
                """A simple method that returns an int"""
                return 42

            @memoize
            def a_property(self):
                """A method decorated with the memoize function"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            # Mock response from TestClass.a_method()
            result = 42
            response = Mock()
            response.return_value = result
            mock_a_method.return_value = response
            tmp = TestClass()

            # Make multiple calls to method to test memoization
            for _ in range(2):
                self.assertEqual(tmp.a_property(), result)
            mock_a_method.assert_called_once()


if __name__ == '__main__':
    """Tests the code in this module"""
    main(verbosity=2)
