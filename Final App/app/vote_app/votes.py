from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from database.models import Post, Vote
from database.schemas import UpdatePost, UserResponse, VoteOutput

from app.users_app.oauth import get_current_user


router = APIRouter(
    tags=['Vote']
)


@router.post("/votes/", status_code=status.HTTP_201_CREATED)
def vote(vote: VoteOutput, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):

    post = db.query(Post).filter(Post.id == vote.post_id).first()
    # print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {vote.post_id} does not exist")
    # print('i am here')
    # vote_query = db.query(Vote)
    vote_query = db.query(Vote).filter(Vote.post_id == vote.post_id, Vote.user_id == current_user.id)
    # print(f'Vote:- {vote_query.first()}')

    # found_vote = vote_query.first()
    if (vote.dir == 1):
        if vote_query.first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {current_user.id} has alredy voted on post {vote.post_id}")
        new_vote = Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "successfully added vote"}
    else:
        if not vote_query.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exist")

        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "successfully deleted vote"}