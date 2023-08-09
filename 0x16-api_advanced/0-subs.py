#!/usr/bin/python3
"""gets the number of subscribers from a subreddit"""
from requests import get


def number_of_subscribers(subreddit):
    about = get('https://reddit.com/r/{}/about.json'.format(subreddit),
                headers={'User-Agent': 'felixhatesbugs'})
    return about.json().get('data', {}).get('subscribers', 0)
