#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request """

from sys import argv
import requests


def main():
    """Python script that takes in a URL and an email, sends a POST request
    """
    url = argv[1]
    response = requests.post(url, data={'email': argv[2]})
    print(response.text)


if __name__ == "__main__":
    main()
