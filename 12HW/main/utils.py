import json




def load_json_data(path):
    with open(path, 'r', encoding="UTF-8") as file:
        return json.load(file)


def search_post_by_substring(substring, path):
    posts = load_json_data(path)
    posts_found = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            posts_found.append(post)
    return posts_found


#print(load_json_data("../posts.json"))
#print(search_post_by_substring("Ага", "../posts.json"))
