from app.database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP

class Posts(Base):
    __tablename__='post'
    __table_args__={'schema': 'crud_schema'}
    id=Column(Integer, primary_key=True, nullable=False)
    title=Column(String, nullable=False)
    content=Column(String, nullable=False)
    published=Column(Boolean, default=True, nullable=False)
    created_at=Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))