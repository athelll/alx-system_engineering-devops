#!/usr/bin/python3
"""gets the top 10 hot posts of a subreddit"""
from requests import get


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {'User-Agent': 'felixhatebugs'}
    param = {'limit': 10}

    top = get(url, headers=header, params=param, allow_redirects=False)
    if top.status_code != 200:
        print("None")
        return

    top = top.json().get('data').get('children')
    [print(x.get('data').get('title')) for x in top]
