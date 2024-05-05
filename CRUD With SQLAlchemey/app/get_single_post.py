from fastapi import APIRouter, status, HTTPException, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.models import Posts
from app.schemas import UserResponse


router=APIRouter()

# To get single post
@router.get('/get_single_post/{id}', response_model=UserResponse)
async def get_single_post(id: int, db: Session=Depends(get_db)):
    get_post=db.query(Posts).filter(Posts.id==id).first()
    if not get_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Post with {id} was not found.')
    print(get_post)
    return get_post