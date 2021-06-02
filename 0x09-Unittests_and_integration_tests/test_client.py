#!/usr/bin/env python3
""" Module that holds parameterize and patch as decorators
"""

import unittest
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import PropertyMock, patch


class TestGithubOrgClient(unittest.TestCase):
    """ Class that holds the tests that verify the
        operation of the githuborgclient,
        Class that inherits from unittest.TestCase
        (Parameterize and patch as decorators)
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org, mock):
        """ Method that test GithubOrgClient.org
            and returns the correct value
        """
        TestClass = GithubOrgClient(org)
        TestClass.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{org}')

    def test_public_repos_url(self):
        """ Method to unit-test GithubOrgClient._public_repos_url,
            the result should be as expected based on the mocked payload,
            (Mocking a property)
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            mock.return_value = {"repos_url": "World"}
            TestClass = GithubOrgClient('org')
            response = TestClass._public_repos_url
            self.assertEqual(response, mock.return_value["repos_url"])
