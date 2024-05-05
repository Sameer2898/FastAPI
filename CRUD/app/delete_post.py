from fastapi import APIRouter, Response, status, HTTPException
from app.common_code import find_post_index, my_posts
from app.database import conn

router = APIRouter()
cursor = conn.cursor()

@router.delete("/delete_post/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("DELETE FROM crud_schema.post WHERE id = (%s) RETURNING *", (str(id)))
    post_index = cursor.fetchone()
    conn.commit()
    # post_index = find_post_index(id)
    print(post_index)
    if post_index == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                        detail = f"Post with {id} is not found.")
    # my_posts.pop(post_index)
    return Response(status_code = status.HTTP_204_NO_CONTENT)