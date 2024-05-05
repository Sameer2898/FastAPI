from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

all_post = []

class Posts(BaseModel):
    user_name: str
    user_id: int
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get('/')
async def hello():
    return {'Data': all_post}
    # return r"Hello i'm fastAPI."

@app.post('/post')
async def post(post: Posts):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10)
    all_post.append(post_dict)
    return {'data': post_dict}