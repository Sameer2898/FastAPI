from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Posts(BaseModel):
    user_name: str
    user_id: int
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get('/')
async def hello():
    return r"Hello i'm fastAPI."

@app.post('/post')
async def post(post: Posts):
    # print(post.dict())
    return post
    # return "Successfully created a new post."