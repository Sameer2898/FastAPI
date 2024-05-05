from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from database.models import Post
from database.schemas import UpdatePost, UserResponse

from app.users_app.oauth import get_current_user

router = APIRouter(
    tags=['Posts']
)


@router.put("/update_post/{id}", response_model=UserResponse)
def update_post(id: int, post: UpdatePost, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    updated_post_query = db.query(Post).filter(Post.id == id)
    
    if updated_post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with {id} is not found.")
        
    if updated_post_query.first().user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authenticated to perform the updation.")
        
    updated_post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return updated_post_query.first()
