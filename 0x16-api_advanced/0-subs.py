#!/usr/bin/python3
"""How many subs"""
import requests


def number_of_subscribers(subreddit):
    """Returns number of subcribers for a given sub reddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'CustomClient/1.0'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return (0)
    r = r.json()
    if 'data' in r:
        return (r.get('data').get('subscribers'))
    return (0)
