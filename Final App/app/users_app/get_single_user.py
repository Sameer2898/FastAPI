from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from database.models import User
from database.schemas import UserOutput


router = APIRouter(
    tags=['Users']
)

# To get single post


@router.get('/get_single_user/{id}', response_model=UserOutput)
async def get_single_user(id: int, db: Session = Depends(get_db)):
    get_user = db.query(User).filter(User.id == id).first()
    if not get_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with {id} was not found.')
    # print(get_user)
    return get_user
