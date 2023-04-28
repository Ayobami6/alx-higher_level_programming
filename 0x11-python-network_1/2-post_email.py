#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request """

from sys import argv
import urllib.request
import urllib.parse


def main():
    """Main function
    """
    url = argv[1]
    email = argv[2]
    values = {'email': email}
    content = urllib.parse.urlencode(values)

    request = urllib.request.Request(url, content.encode('ascii'))
    with urllib.request.urlopen(request) as response:
        html = response.read()
        print(html.decode('utf-8'))


if __name__ == "__main__":
    main()
