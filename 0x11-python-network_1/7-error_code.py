#!/usr/bin/python3
"""Python script that takes in a URL, sends a
    request to the URL and displays the body of the response.
    """
from sys import argv
import requests


def main():
    """ Main Function
    """
    url = argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    main()
