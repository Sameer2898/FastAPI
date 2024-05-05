from fastapi import APIRouter, status, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.models import Posts
from app.schemas import CreatePost, UserResponse

router=APIRouter()


# To create posts
@router.post('/create_post', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_post(post: CreatePost, db: Session=Depends(get_db)):
    created_post = Posts(**post.dict())
    db.add(created_post)
    db.commit()
    db.refresh(created_post)
    return created_post