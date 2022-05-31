import json



def get_posts(path):
    with open(path, 'r', encoding='UTF-8') as file:
        return json.load(file)

def get_post_by_substrind(s, path):
    posts = get_posts(path)
    finded_posts = []
    for post in posts:
        if s.lower() in post['content'].lower():
            finded_posts.append(post)
    return finded_posts


#print(get_posts(POST_PATH))



