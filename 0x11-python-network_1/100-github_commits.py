#!/usr/bin/python3
"""
a Python script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url)
    for i in response.json()[:10]:
        SHA = i.get('SHA') # SHA- typically refers to a Secure Hash Algorithm
        author_name = i.get('commit').get('author').get('name')
        print('{}: {}'.format(SHA, author_name))

