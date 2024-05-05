from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from database.models import Post
from database.schemas import CreatePost, UserResponse

from app.users_app.oauth import get_current_user

router = APIRouter(
    tags=['Posts']
)

# To create posts


@router.post('/create_post', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_post(post: CreatePost, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    created_post = Post(user_id=current_user.id, **post.dict())
    db.add(created_post)
    db.commit()
    db.refresh(created_post)
    return created_post
