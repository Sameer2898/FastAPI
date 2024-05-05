from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    published: bool=True

class CreatePost(PostBase):
    pass

class UpdatePost(PostBase):
    title: str
    content: str
    published: bool

class UserResponse(PostBase):
    pass

    class Config:
        orm_mode=True