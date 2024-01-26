#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
The first argument will be your username
The second argument will be your password
(in your case, a personal access token as password)
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    signin = requests.Session()
    signin.auth = (argv[1], argv[2])
    req = signin.get(url)
    try:
        print('{}'.format(req.json()['id']))
    except:
        print("None")
