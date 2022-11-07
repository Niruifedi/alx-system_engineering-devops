#!/usr/bin/python3

"""function that queries the Reddit API"""
import requests
import sys


def top_ten(subreddit):
    """
    Returns: top ten post in a given subreddit
    or none if queried subreddit is invalid
    """
    headers = {'User-agent': 'hbnb_test'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        titles = response.json().get('data').get('children')
        for title_ in titles:
            print(title_.get('data').get('title'))
    else:
        print(None)
