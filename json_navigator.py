"""
Module for Twitter Data json navigation
"""
import json
from pprint import pprint
import requests


def twitter_api():
    """
    Get json from twitter
    """
    tweet_tag = input("Enter twitter tag: @")
    base_url = "https://api.twitter.com/"

    bearer_token = ""

    search_url = '{}1.1/friends/list.json'.format(base_url)

    search_headers = {
        'Authorization': 'Bearer {}'.format(bearer_token)
    }

    search_params = {
        'screen_name': f'@{tweet_tag}',
        'count': 15
    }

    response = requests.get(
        search_url, headers=search_headers, params=search_params)
    return response.json()['users']


def find_by_keys(twitter_dict: str):
    """
    Extract values from json by keys.

    """
    num = int(input("Enter a random number and recieve info about one friend: "))
    twitter = twitter_dict[num]
    while True:
        if isinstance(twitter, dict):

            print("---"*10)
            pprint(list(twitter.keys()))
            print("---"*10)
            while True:
                key = input("Pick an existing key and recieve info: ")
                if key in twitter.keys():
                    print("---"*10)
                    pprint(twitter[key])
                    print("---"*10)
                    if isinstance(twitter[key], dict):
                        print("---"*10)
                        pprint(list(twitter[key]))
                        print("---"*10)
                        twitter = twitter[key]
                    else:
                        return twitter[key]

                else:
                    print("Wrong key!")
                    endpoint = input("Do you want to end? (y/n) ")
                    if endpoint == "y":
                        break


if __name__ == "__main__":
    find_by_keys(twitter_api())
