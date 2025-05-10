# Nicholas Smith
# 10 May 2025
# Lab 17: GitHub API
# This program retrieves the top Python repositories from GitHub and visualizes them using Plotly.

import json

import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"
url += "?q=language:C#+stars:>10000&sort=stars&order=desc"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

fig = px.bar(x=repo_names, y=stars)
fig.show()