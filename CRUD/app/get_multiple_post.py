from fastapi import APIRouter
# from app.common_code import my_posts
from app.database import conn

router = APIRouter()
cursor = conn.cursor()

# To get multiple posts
@router.get('/get_multiple_post')
async def get_multiple_post():
    cursor.execute("SELECT * FROM crud_schema.post;")
    posts = cursor.fetchall()
    # print(posts)
    return {'data': posts}