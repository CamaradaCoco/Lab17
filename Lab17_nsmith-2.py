# Nicholas Smith
# 10 May 2025
# Lab 17 #2
# This program retrieves the top C# repositories from GitHub and visualizes them using Plotly.

import requests
import plotly.express as px

# Set up the API request
url = "https://api.github.com/search/repositories"
url += "?q=language:C#+stars:>10000&sort=stars&order=desc"

# Set up the headers for the request
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Check if the request was successful
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Process the response
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars_count = repo_dict['stargazers_count']
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}: {description}"
    hover_texts.append(hover_text)

# Create a bar chart using Plotly
title = "GitHub C# Repositories With Over 10,000 Stars"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts, color_discrete_sequence=["red"])
fig.update_layout(
    title_font_size=30, 
    xaxis_title_font_size=20, 
    yaxis_title_font_size=20,
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,)
fig.show()