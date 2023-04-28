#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request """

from sys import argv
import urllib.request


def main():
    """Python script that takes in a URL and an email, sends a POST request
    """
    url = argv[1]
    response = urllib.request.Request(url)
    with urllib.request.urlopen(response) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    main()
