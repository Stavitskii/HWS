import json



def get_posts(path):
    with open(path, 'r', encoding='UTF-8') as file:
        return json.load(file)

def get_post_by_substring(posts,s):
    posts = get_posts(posts)

    found_posts = []
    for post in posts:
        if s.lower() in post['content'].lower():
            found_posts.append(post)
    return found_posts


#print(get_posts('../posts.json'))
#print(get_post_by_substring('ага', '../posts.json'))



