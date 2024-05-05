from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from database.models import User
from database.schemas import CreateUser, UserOutput

from app.users_app.utils import password_hashing

router = APIRouter(
    tags=['Users']
)

# To create posts


@router.post('/user', status_code=status.HTTP_201_CREATED, response_model=UserOutput)
async def create_post(user: CreateUser, db: Session = Depends(get_db)):
    hashed_password = password_hashing(user.password)
    user.password = hashed_password
    created_user = User(**user.dict())
    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    return created_user
