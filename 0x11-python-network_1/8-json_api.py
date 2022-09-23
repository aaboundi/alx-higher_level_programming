#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""
import sys
import requests


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post(url, data={'q': q})
    try:
        json_content = response.json()
        if json_content:
            print("[{}] {}".format(json_content.get('id'), json_content.get('name')))
        else:
            print('No result')
    except ValueError:
        print('No a valid JSON')
