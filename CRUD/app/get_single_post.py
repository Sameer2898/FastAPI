from fastapi import APIRouter, Response, status, HTTPException
from app.common_code import find_post
from app.database import conn

router = APIRouter()
cursor = conn.cursor()

# To get single post
@router.get('/get_single_post/{id}')
async def get_single_post(id: int, response: Response):
    cursor.execute("SELECT * FROM crud_schema.post WHERE id = (%s)", (str(id)))
    get_post = cursor.fetchone()
    # get_post = find_post(id)
    if not get_post:
        # This is the convinent way. We can use this one too but the most suitable way is which is not commented.
        # response.status_code = status.HTTP_404_NOT_FOUND 
        # return {'Post_detail': f'Post with {id} was not found.'}
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f'Post with {id} was not found.')
    print(get_post)
    return {'Post_detail': get_post}