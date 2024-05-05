from fastapi import APIRouter, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.models import Posts
from app.schemas import UserResponse
from typing import List

router=APIRouter()

# To get multiple posts
@router.get('/get_multiple_post/', response_model=List[UserResponse])
async def get_multiple_post(db: Session=Depends(get_db)):
    get_post=db.query(Posts).all()
    return get_post