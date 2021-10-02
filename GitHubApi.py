# -*- coding: utf-8 -*-
"""
The primary goal of this file is to implement the githubAPI class tool.

@author: Margaret Lehmann
"""
import requests
import json


def GitHubAPI(github_user_id):
    """
    githubAPI
    """
    commit_data = []
    repos = requests.get("https://api.github.com/users/" +
                         github_user_id + "/repos").json()
    for repo in repos:
        commits = requests.get("https://api.github.com/repos/" +
                               github_user_id + "/" + repo["name"] + "/commits").json()
        commit_data.append(
            "Repo: " + repo["name"] + " Number of commits: " + str(len(commits)))

    return commit_data
