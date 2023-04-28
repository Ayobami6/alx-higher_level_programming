#!/usr/bin/python3
"""a Python script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You dont need to check arguments passed to the script (number or type)
"""

from sys import argv
import requests


def main():
    """ Main Function
    """
    # assessing commit api endpoint for a given repo
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    # getting the response from the api
    response = requests.get(url)
    # jsonify the response
    commits = response.json()

    try:
        for i in range(10):
            print("{}: {}".
                  format(commits[i]['sha'],
                         commits[i]['commit']['author']['name']))
    except IndexError:
        pass


if __name__ == "__main__":
    main()
