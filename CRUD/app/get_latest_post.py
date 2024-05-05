from fastapi import APIRouter
from app.common_code import my_posts

router = APIRouter()

# To fetch latest posts
@router.get("/get_latest_post")
def get_latest_post():
    latest_post = my_posts[len(my_posts) - 1]
    return {'latest_post': latest_post}