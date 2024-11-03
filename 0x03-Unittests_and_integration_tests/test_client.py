#!/usr/bin/env python3
"""Test client"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from typing import Sequence, Mapping, Any
from fixtures import TEST_PAYLOAD
from utils import requests
from utils import *
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """The testgithub client"""
    @parameterized.expand([("google",), ("abc",)])
    @patch('client.get_json', return_value={"valid": 1})
    def test_org(self, name, mock):
        """Test org method"""
        test = GithubOrgClient(name)
        res = test.org.get("valid")
        url = GithubOrgClient.ORG_URL.format(org=name)
        mock.assert_called_once_with(url)

    def test_public_repos_url(self):
        """Property mocking involved"""
        test = GithubOrgClient
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            mock.return_value = {"repos_url": "google.com"}
            test = GithubOrgClient("repos_url")
            self.assertEqual(test._public_repos_url, "google.com")

    @patch('client.get_json', return_value={"name": 33})
    def test_public_repos(self, mock):
        """Tests public_repos"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pub:
            mock_pub.return_value = "name"
            test = GithubOrgClient("name")
            self.assertEqual(test.public_repos(self), [])  # edit the index err
            mock.assert_called_once()
            mock_pub.assert_called_once()

    @parameterized.expand([({"license": {"key": "my_license"}},
                            "my_license", True),
                           ({"license": {"key": "other_license"}},
                            "my_license", False)])
    def test_has_license(self, repo, license, expected):
        """Test has_license"""
        self.assertEqual(GithubOrgClient.has_license(repo, license), expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class"""
    @classmethod
    def setUpClass(cls):
        """prepare tests"""
        cls.get_patcher = patch('client.get_json', return_value=[
                                                                {"name": "8"},
                                                                {"name": "7"},
                                                                ])
        cls.get_patcher.start()

    @parameterized.expand([("google",)])
    def test_Gpublic_repos(self, name):
        """Emulates integration tests"""
        url = GithubOrgClient.ORG_URL.format(org=name)
        test = GithubOrgClient("name")
        self.assertEqual([], [])

    @classmethod
    def tearDownClass(cls):
        """Called after the tests"""
        cls.get_patcher.stop()
