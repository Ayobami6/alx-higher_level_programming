#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
    """

import requests


def main():
    """Python script that fetches https://intranet.hbtn.io/status
    """
    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    main()
