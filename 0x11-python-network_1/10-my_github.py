#!/usr/bin/python3
"""Takes in Github credentials (username and password) and uses the Github API
to display an id"""
import sys
import requests


if __name__ == '__main__':
    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    if r.status_code >= 400:
        print('None')
    else:
        print(r.json().get('id'))
