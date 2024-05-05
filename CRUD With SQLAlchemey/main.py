from fastapi import FastAPI
from app.create_post import router as create_post
from app.get_single_post import router as get_single_post
from app.get_multiple_post import router as get_multiple_post
from app.update_post import router as update_post
from app.delete_post import router as delete_post

app = FastAPI()

app.include_router(create_post)
app.include_router(get_single_post)
app.include_router(get_multiple_post)
app.include_router(update_post)
app.include_router(delete_post)