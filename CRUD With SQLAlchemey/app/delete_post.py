from fastapi import APIRouter, Response, status, HTTPException, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.models import Posts

router=APIRouter()

@router.delete("/delete_post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session=Depends(get_db)):
    deleted_post=db.query(Posts).filter(Posts.id==id)
    if deleted_post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post with {id} is not found.")
    deleted_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)