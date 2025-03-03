#!/usr/bin/env python3
""" File for test client.py
"""
import unittest
from client import GithubOrgClient
from utils import get_json
from unittest.mock import patch, PropertyMock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ Class TestGithubOrgClient
    """
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False})
    ])
    @patch("client.get_json")
    def test_org(self, org, test_payload, mock_get_json):
        """ Test org method
        """
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org)

        self.assertEqual(client.org, test_payload)
        mock_get_json.assert_called_once_with
        (f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self):
        """ Test _public_repos_url
        """
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, payload["repos_url"])
