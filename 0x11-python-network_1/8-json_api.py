#!/usr/bin/python3
"""Python script that takes in a letter and sends a
    POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
    """
from sys import argv
import requests


def main():
    """ Main Function
    """
    q = argv[1] if len(argv) > 1 else ""
    q_api = {'q': q}

    response = requests.post("http://0.0.0.0:5000/search_user", data=q_api)
    try:
        response_json = response.json()
        if response_json:
            print("[{}] {}".format(response_json['id'], response_json['name']))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
