from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from database.models import Post

from app.users_app.oauth import get_current_user

router = APIRouter(
    tags=['Posts']
)


@router.delete("/delete_post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    deleted_post_query = db.query(Post).filter(Post.id == id)
    # deleted_post = deleted_post_query.first()
    
    if deleted_post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with {id} is not found.")
    
    if deleted_post_query.first().user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authenticated to perform the deletion.")
        
    deleted_post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
