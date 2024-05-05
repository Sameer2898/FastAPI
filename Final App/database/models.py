from sqlalchemy.sql.expression import text
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

from database.db import Base

# Posts Table


class Post(Base):
    __tablename__ = 'posts'
    __table_args__ = {'schema': 'crud_schema'}
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey(
        'crud_schema.users.id', ondelete="CASCADE"), nullable=False)

    user_relationship = relationship('User')

# USer Table


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'crud_schema'}
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

# Vote table


class Vote(Base):
    __tablename__ = "votes"
    __table_args__ = {'schema': 'crud_schema'}
    post_id = Column(Integer, ForeignKey(
        "crud_schema.posts.id", ondelete="CASCADE"), primary_key=True)
    user_id = Column(Integer, ForeignKey(
        "crud_schema.users.id", ondelete="CASCADE"), primary_key=True)
    likes = Column(Integer)
