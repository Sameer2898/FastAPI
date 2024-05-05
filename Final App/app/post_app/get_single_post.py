from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from database.models import Post
from database.schemas import UserResponse

from app.users_app.oauth import get_current_user

router = APIRouter(
    tags=['Posts']
)

# To get single post


@router.get('/get_single_post/{id}', response_model=UserResponse)
async def get_single_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    get_post = db.query(Post).filter(Post.id == id).first()
    if not get_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with {id} was not found.')
    # print(get_post)
    return get_post
