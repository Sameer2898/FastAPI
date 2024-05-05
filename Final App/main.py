from fastapi import FastAPI

from database.db import Base, engine

from app.post_app.create_post import router as create_post
from app.post_app.get_single_post import router as get_single_post
from app.post_app.get_multiple_post import router as get_multiple_post
from app.post_app.update_post import router as update_post
from app.post_app.delete_post import router as delete_post

from app.users_app.create_user import router as create_user
from app.users_app.get_single_user import router as get_single_user
from app.users_app.get_multiple_user import router as get_multiple_user
from app.users_app.login_user import router as user_login

from app.vote_app.votes import router as vote

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Post App
app.include_router(create_post)
app.include_router(get_single_post)
app.include_router(get_multiple_post)
app.include_router(update_post)
app.include_router(delete_post)

# User App
app.include_router(create_user)
app.include_router(get_single_user)
app.include_router(get_multiple_user)
app.include_router(user_login)

# Vote App
app.include_router(vote)
