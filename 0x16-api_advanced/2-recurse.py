#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles
"""
from requests import get


def recurse(subreddit, hot_list=[], after=''):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {'User-Agent': 'felixhatesbugs'}
    param = {'after': after, 'limit': 100}

    hot = get(url, headers=header, params=param, allow_redirects=False)
    if hot.status_code != 200:
        return None

    hot = hot.json().get('data')
    after = hot.get('after')

    for x in hot.get('children'):
        hot_list.append(x.get('data').get('title'))

    if after is not None:
        recurse(subreddit, hot_list, after)
    return hot_list
