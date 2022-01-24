import requests
from .repo import Repository

# URL = 'https://api.github.com/users/github/repos'


def fetch_repos(name):
    URL = f'https://api.github.com/users/{name}/repos'
    req = requests.get(URL)
    for data in req.json():
        Repository(data)
    return data
