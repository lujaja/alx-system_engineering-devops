#!/usr/bin/python3
"""How many subs"""
import requests


def number_of_subscribers(subreddit):
    """Returns number of subcribers for a given sub reddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            'AppleWebKit/537.36 (KHTML, like Gecko)'
            'Chrome/91.0.4472.124 Safari/537.36'
        }
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        data = r.json()
        return int(data['data']['subscribers'])
    else:
        return 0
