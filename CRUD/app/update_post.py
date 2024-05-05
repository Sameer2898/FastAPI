from fastapi import APIRouter, status, HTTPException
from app.common_code import find_post_index, my_posts, Posts
from app.database import conn

router = APIRouter()
cursor = conn.cursor()

@router.put("/update_post/{id}")
def update_post(id: int, post: Posts):
    cursor.execute("UPDATE crud_schema.post SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *", (post.title, post.content, post.published, str(id)))
    print(post)
    post_index = cursor.fetchone()
    conn.commit()
    if post_index == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                        detail = f"Post with {id} is not found.")
    # post_dict = post.dict()
    # post_dict['id'] = id
    # my_posts[post_index] = post_dict
    return {'data': post_index}