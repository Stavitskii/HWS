import json



def get_posts(path, pic, content):
    with open(path, 'r', encoding='UTF-8') as file:
        posts =json.load(file)
        post_dic = {'pic':pic, 'content':content}
        posts.append(post_dic)
    with open(path, 'w', encoding='UTF-8') as written_file:
        json.dump(posts, written_file, indent=4, ensure_ascii=False)


