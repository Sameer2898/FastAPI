from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from database.models import Post
from database.schemas import UserResponse

router = APIRouter(
    tags=['Posts']
)

# To get multiple posts
@router.get('/get_multiple_post/', response_model=List[UserResponse])
async def get_multiple_post(db: Session = Depends(get_db), limit: int = 10):
    get_post = db.query(Post).limit(limit).all()
    return get_post
