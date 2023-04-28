#!/usr/bin/python3
"""Python script that takes your GitHub
    credentials (username and password) and uses the GitHub API
    to display your id
    """
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


def main():
    """ Main Function
    """
    auth = HTTPBasicAuth(argv[1], argv[2])
    response = requests.get('https://api.github.com/user', auth=auth)
    print(response.json().get('id'))


if __name__ == "__main__":
    main()
