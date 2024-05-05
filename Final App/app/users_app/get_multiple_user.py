from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from database.models import User
from database.schemas import UserOutput

router = APIRouter(
    tags=['Users']
)

# To get multiple posts


@router.get('/get_multiple_user/', response_model=List[UserOutput])
async def get_multiple_user(db: Session = Depends(get_db)):
    get_post = db.query(User).all()
    return get_post
