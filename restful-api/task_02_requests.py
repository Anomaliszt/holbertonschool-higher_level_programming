#!/usr/bin/python3
"""
fetch_and_print_posts()
fetch_and_save_posts()
"""


import requests
import csv


def fetch_and_print_posts():
    """  print out the titles of all the posts """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """ CSV file called posts.csv with columns to the dictionary keys. """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()

        with open('posts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            for post in posts:
                writer.writerow({'id': post['id'], 'title': post['title'], 'body': post['body']})

