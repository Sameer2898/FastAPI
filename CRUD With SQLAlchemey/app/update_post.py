from fastapi import APIRouter, status, HTTPException, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.models import Posts
from app.schemas import UpdatePost, UserResponse

router=APIRouter()

@router.put("/update_post/{id}", response_model=UserResponse)
def update_post(id: int, post: UpdatePost, db: Session=Depends(get_db)):
    updated_post_query=db.query(Posts).filter(Posts.id==id)
    if updated_post_query.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post with {id} is not found.")
    updated_post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return updated_post_query.first()