from fastapi import FastAPI, Body, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

all_post = []

class Posts(BaseModel):
    id: int
    title: str
    content: str
    published: bool = True
    
try:
    conn = psycopg2.connect(host = 'localhost', database = 'postgres', user = 'postgres', password = 'don\'tdothis', cursor_factory = RealDictCursor)
    print('Established Database Connection.')
except Exception as e:
    print(f'Error while establishing connection:-\n{e}')

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

# To create posts
@app.post('/create_post', status_code = status.HTTP_201_CREATED)
async def create_post(post: Posts):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10)
    all_post.append(post_dict)
    return {'data': post_dict}

# To get multiple posts
@app.get('/get_multiple_post')
async def get_multiple_post():
    return {'data': my_posts}

# To get single post
@app.get('/get_single_post/{id}')
async def get_single_post(id: int, response: Response):
    get_post = find_post(id)
    if not get_post:
        # This is the convinent way. We can use this one too but the most suitable way is which is not commented.
        # response.status_code = status.HTTP_404_NOT_FOUND 
        # return {'Post_detail': f'Post with {id} was not found.'}
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f'Post with {id} was not found.')
    print(get_post)
    return {'Post_detail': get_post}

# To fetch latest posts
@app.get("/get_latest_post")
def get_latest_post():
    latest_post = my_posts[len(my_posts) - 1]
    return {'latest_post': latest_post}

@app.delete("/delete_post/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    post_index = find_post_index(id)
    print(post_index)
    if post_index == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                        detail = f"Post with {id} is not found.")
    my_posts.pop(post_index)
    return Response(status_code = status.HTTP_204_NO_CONTENT)

@app.put("/update_post/{id}")
def update_post(id: int, post: Posts):
    print(post)
    post_index = find_post_index(id)
    if post_index == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                        detail = f"Post with {id} is not found.")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[post_index] = post_dict
    return {'data': post_dict}

# Next:- FastAPI automatic documentation video number 20
