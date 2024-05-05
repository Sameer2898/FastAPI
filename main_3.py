from fastapi import FastAPI, Body

app = FastAPI()

@app.get('/')
async def hello():
    return r"Hello i'm fastAPI."

@app.post("/create_posts")
async def user_message(data: dict=Body(...)):
    print(data)
    return f"Created a new post. User_Name{data['user_name']}.Message{data['message']}"