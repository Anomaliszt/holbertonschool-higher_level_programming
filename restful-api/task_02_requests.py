#!/usr/bin/python3


import requests
import csv

def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(['Title'])

def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()

        with open('posts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            for post in posts:
                writer.writerow(post)
