from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from jose import jwt, JWTError
from datetime import datetime, timedelta

from database.schemas import TokenData
from database.db import get_db
from database.models import User

# from  app.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=2

def create_access_token(data: dict):
    data_to_encode = data.copy()
    expire_time = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # data_to_encode.update({'expire': expire_time})
    # print(data_to_encode)
    encodeed_jwt = jwt.encode(data_to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encodeed_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = decoded_token.get('user_id')
        # print(id)
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=str(id))

    except JWTError:
        raise credentials_exception
    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail='Could not validate credentilas.', 
                                          headers={'WWW-Authenticate': 'Bearer'})
    token = verify_access_token(token, credentials_exception)
    # print(f'Token:{token}')
    user = db.query(User).filter(User.id == token.id).first()
    return user
