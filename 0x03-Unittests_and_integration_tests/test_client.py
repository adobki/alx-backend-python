#!/usr/bin/env python3
"""This module showcases unit testing in Python with parameterized"""
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from unittest import TestCase, main
from unittest.mock import Mock, PropertyMock, patch
import client
import utils


class TestGithubOrgClient(TestCase):
    """Unittests for client.GithubOrgClient class"""
    @parameterized.expand([
        ('google', True),
        ('abc', False)
    ])
    @patch('client.get_json')
    def test_org(self, org, status, mock_get_json):
        """Test org method"""
        # Mock client.get_json method
        org_json = {'login': org, 'name': org, 'is_verified': status}
        mock_get_json.return_value = org_json

        # Test org method and make sure it calls get_json() only once
        test_client = client.GithubOrgClient(org)
        self.assertEqual(test_client.org, org_json)
        mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """Test _public_repos_url method"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            url = 'https://api.github.com/orgs/google/repos'
            mock_org.return_value = {'repos_url': url}

            # Test mocked property
            test_client = client.GithubOrgClient('google')
            self.assertEqual(test_client._public_repos_url, url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos method"""
        # Mock client.get_json method
        repo_json = [{'name': 'Google'}, {'name': 'login'},
                     {'name': 'is_verified'}, {'name': 'adobki'}]
        mock_get_json.return_value = repo_json

        # Mock GithubOrgClient._public_repos_url property
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_url:
            mock_url.return_value = 'https://api.github.com/orgs/google/repos'

            # Test GithubOrgClient.public_repos
            names = [repo['name'] for repo in repo_json]
            test_client = client.GithubOrgClient('google')
            self.assertEqual(test_client.public_repos(), names)

            # Test that the mocked objects were called only once
            mock_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license static method"""
        self.assertEqual(
            client.GithubOrgClient.has_license(repo, license_key), expected
        )


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(TestCase):
    """Integration tests for client.GithubOrgClient class"""
    @classmethod
    def setUpClass(cls):
        """Prepares the test fixture"""
        cls.get_patcher = patch('requests.get')
        cls.MockGet = cls.get_patcher.start()

        def get_response(url):
            """Helper function for mocked object's side effects"""
            response = Mock()
            if url.endswith('/repos'):
                response.json.return_value = cls.repos_payload
            else:
                response.json.return_value = cls.org_payload
            return response

        cls.MockGet.side_effect = get_response

    @classmethod
    def tearDownClass(cls):
        """Performs cleanup after test fixture"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method through integration testing"""
        self.assertEqual(client.GithubOrgClient('google').public_repos(),
                         self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method with a specific license"""
        self.assertEqual(
            client.GithubOrgClient('adobki').public_repos('apache-2.0'),
            self.apache2_repos
        )


if __name__ == '__main__':
    """Tests the code in this module"""
    main(verbosity=2)
