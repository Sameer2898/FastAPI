from pydantic import BaseModel

class Posts(BaseModel):
    # id: int
    title: str
    content: str
    published: bool = True

my_posts = [
            {'id': 1, 'title': 'first_post', 'content': 'This is first post.'},
            {'id': 2, 'title': 'second_post', 'content': 'This is second post.'}
            ]

def find_post(id):
    for i in my_posts:
        if i['id'] == id:
            return i

def find_post_index(id):
    for index, post in enumerate(my_posts):
        if post['id'] == id:
            return index