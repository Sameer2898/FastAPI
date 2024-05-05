from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello():
    return r"Hello i'm fastAPI."