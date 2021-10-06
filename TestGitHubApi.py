# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to test the github API class

@author: Margaret Lehmann
"""

import unittest

from unittest import mock

from unittest.mock import patch

import GitHubApi
from GitHubApi import GitHubAPI


class TestGitHubAPI(unittest.TestCase):
    """
    Testing the git hub api tool
    Correct results for mlehmann2

    Repo: bingbites Number of commits: 2
    Repo: BUMS Number of commits: 30
    Repo: GitHubApiTool567 Number of commits: 8
    Repo: hw-acceptance-unit-test-cycle Number of commits: 30
    Repo: hw-sinatra-saas-hangperson Number of commits: 30
    Repo: HW00-HelloWorld Number of commits: 2
    Repo: HW01-Triangles Number of commits: 2
    Repo: HW02a-LegacyTesting Number of commits: 11
    Repo: Student-Repository Number of commits: 17

    """

    @patch('GitHubApi.GitHubAPI')
    def testNumRepos(self, mock_get):
        mock_get.return_value = \
            ['Repo: bingbites Number of commits: 2',
             'Repo: BUMS Number of commits: 30',
             'Repo: GitHubApiTool567 Number of commits: 8',
             'Repo: hw-acceptance-unit-test-cycle Number of commits: 30',
             'Repo: hw-sinatra-saas-hangperson Number of commits: 30',
             'Repo: HW00-HelloWorld Number of commits: 2',
             'Repo: HW01-Triangles Number of commits: 2',
             'Repo: HW02a-LegacyTesting Number of commits: 11',
             'Repo: Student-Repository Number of commits: 17']

        self.assertEqual(len(GitHubApi.GitHubAPI('mlehmann2')), 9)

    @patch('GitHubApi.GitHubAPI')
    def testCorrectResults(self, mock_get):
        mock_get.return_value = \
            ['Repo: bingbites Number of commits: 2',
             'Repo: BUMS Number of commits: 30',
             'Repo: GitHubApiTool567 Number of commits: 8',
             'Repo: hw-acceptance-unit-test-cycle Number of commits: 30',
             'Repo: hw-sinatra-saas-hangperson Number of commits: 30',
             'Repo: HW00-HelloWorld Number of commits: 2',
             'Repo: HW01-Triangles Number of commits: 2',
             'Repo: HW02a-LegacyTesting Number of commits: 11',
             'Repo: Student-Repository Number of commits: 17']
        results = GitHubApi.GitHubAPI('mlehmann2')
        self.assertEqual(results[0], "Repo: bingbites Number of commits: 2")
        self.assertEqual(results[1], "Repo: BUMS Number of commits: 30")
        self.assertEqual(
            results[2], "Repo: GitHubApiTool567 Number of commits: 8")
        self.assertEqual(
            results[3], "Repo: hw-acceptance-unit-test-cycle Number of commits: 30")
        self.assertEqual(
            results[4], "Repo: hw-sinatra-saas-hangperson Number of commits: 30")
        self.assertEqual(
            results[5], "Repo: HW00-HelloWorld Number of commits: 2")
        self.assertEqual(
            results[6], "Repo: HW01-Triangles Number of commits: 2")
        self.assertEqual(
            results[7], "Repo: HW02a-LegacyTesting Number of commits: 11")
        self.assertEqual(
            results[8], "Repo: Student-Repository Number of commits: 17")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
