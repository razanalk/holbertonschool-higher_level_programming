#!/usr/bin/python3
import csv
import requests


def fetch_and_print_posts():
    """Fetch posts from the API and print their titles."""

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        for post in response.json():
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts from the API and save them to posts.csv."""

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    if response.status_code == 200:
        posts = response.json()

        with open(
            "posts.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=["id", "title", "body"]
            )

            writer.writeheader()

            for post in posts:
                writer.writerow({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                })
