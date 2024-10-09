#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """Fetch and print the titles of posts from JSONPlaceholder."""

    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"{post['title']}")  # Print only titles


def fetch_and_save_posts():
    """Fetch posts and save them to a CSV file."""
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        struct = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        with open('posts.csv', mode='w', newline='') as csv_file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write the header
            writer.writeheader()

            # Write the rows
            for post in struct:
                writer.writerow(post)


fetch_and_print_posts()
fetch_and_save_posts()
