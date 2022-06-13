import json
from exceptions import *



def get_posts(path):
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError



def get_post_by_substring(posts,s):
    posts = get_posts(posts)

    found_posts = []
    for post in posts:
        if s.lower() in post['content'].lower():
            found_posts.append(post)
    return found_posts





