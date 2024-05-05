from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint


# Post


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(PostBase):
    pass


class UpdatePost(PostBase):
    pass

class OwnerDetails(BaseModel):
    email: EmailStr

class UserResponse(PostBase):
    id: int
    created_at: datetime
    user_id: int
    # user_details: OwnerDetails

    class Config:
        orm_mode = True

# Users


class CreateUser(BaseModel):
    email: EmailStr
    password: str


class UserOutput(BaseModel):
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


# Vote
class VoteOutput(BaseModel):
    post_id: int
    dir: int
    # likes: int