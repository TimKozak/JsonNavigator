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

    bearer_token = "AAAAAAAAAAAAAAAAAAAAAIKvMwEAAAAAGfXtAizYuenmkYuQLZ4qCDL%2F3n8%3D0Bqy4HA6TVWqzcYq7Nk9UK0slRiRyVZvlEBtpyowkdXOupLBNf"

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
    twitter = twitter_dict
    while True:

        if isinstance(twitter, dict):
            try:
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

                elif isinstance(twitter[key], list):
                    print("---"*10)
                    pprint(twitter[key])
                    print("---"*10)
                    twitter = twitter[key]

                else:
                    return twitter[key]
            except KeyError:
                print("Invalid key")
                endpoint = input("Do you want to end? (y/n) ")
                if endpoint == "y":
                    break

        elif isinstance(twitter, list):
            try:
                index = int(
                    input("Pick an existing index and recieve info: "))
                if index in range(len(twitter)):
                    print("---"*10)
                    pprint(twitter[index])
                    print("---"*10)

                if isinstance(twitter[index], dict):
                    print("---"*10)
                    pprint(list(twitter[index]))
                    print("---"*10)
                    twitter = twitter[index]

                elif isinstance(twitter[index], list):
                    print("---"*10)
                    pprint(twitter[index])
                    print("---"*10)
                    twitter = twitter[index]

                else:
                    return twitter[index]
            except IndexError:
                print("Invalid index")
                endpoint = input("Do you want to end? (y/n) ")
                if endpoint == "y":
                    break


if __name__ == "__main__":
    find_by_keys(twitter_api())
