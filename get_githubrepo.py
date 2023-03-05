import requests
from pprint import pprint
import os

url = "https://api.github.com/user/repos"

header = {
  'Accept': 'application/vnd.github+json',
  'X-GitHub-Api-Version': '2022-11-28',
  'Authorization': f"Bearer {os.environ['GITHUB_TOKEN']}"
}

repos = requests.get(url, headers=header).json()

for repo in repos:
    print(f"id:{repo['id']}\n name:{repo['name']}\n repo_url:{repo['html_url']} \n private:{repo['private']}\n")