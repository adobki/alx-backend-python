#!/usr/bin/env python3
"""This module showcases unit testing in Python with parameterized"""
from parameterized import parameterized
from unittest import TestCase, main
from unittest.mock import patch
import client


class TestGithubOrgClient(TestCase):
    """Unittests for client.GithubOrgClient class"""
    @parameterized.expand([
        ('google', ),
        ('abc', )
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_get_json):
        """Test parameters"""
        # Mock client.get_json method
        org_json = {'login': org, 'name': org, 'is_verified': True}
        mock_get_json.return_value = org_json

        # Test org method and make sure it calls get_json() only once
        test_client = client.GithubOrgClient(org)
        self.assertEqual(test_client.org, org_json)
        mock_get_json.assert_called_once()


if __name__ == '__main__':
    """Tests the code in this module"""
    main(verbosity=2)
