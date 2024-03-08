#!/usr/bin/python3
"""How many subs"""
import requests


def top_ten(subreddit):
    """Returns number of subcribers for a given sub reddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=9".format(subreddit)
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            "AppleWebKit/537.36 (KHTML, like Gecko)"
            "Chrome/91.0.4472.124 Safari/537.36"
        }
    r = requests.get(
            url,
            headers=headers,
            allow_redirects=False)
    if r.status_code != 200:
        print(None)
        return
    try:
        data = r.json()
        posts = data['data']['children']
        titles = [post['data']['title'] for post in posts]
        if titles:
            [print(title) for title in titles]
    except Exception as err:
        print(None)
