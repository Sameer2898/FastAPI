from fastapi import APIRouter, status
# from random import randrange
from app.common_code import Posts
from app.database import conn

router = APIRouter()
cursor = conn.cursor()
all_post = []

# To create posts
@router.post('/create_post', status_code = status.HTTP_201_CREATED)
async def create_post(post: Posts):
    cursor.execute("INSERT INTO crud_schema.post (title, content, published) VALUES (%s, %s, %s) RETURNING *", (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit();
    # post_dict = post.dict()
    # post_dict['id'] = randrange(0, 10)
    # all_post.append(post_dict)
    return {'data': new_post}