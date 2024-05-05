from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database.db import get_db
from database.models import User
from database.schemas import UserLogin

from app.users_app.utils import verify_password
from app.users_app.oauth import create_access_token

router = APIRouter(
    tags=['Users']
)

# To login user


@router.post('/login')
async def user_login(login_model: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_details = db.query(User).filter(
        User.email == login_model.username).first()
    # print(type(user_details.id))

    if not user_details:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'Invalid Credentials!')

    if not verify_password(login_model.password, user_details.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'Invalid Credentials!')
    access_token = create_access_token(data={'user_id': user_details.id})
    return {'access_token': access_token, 'token_type': 'bearer'}
