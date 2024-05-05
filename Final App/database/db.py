from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATAABASE_URL='postgresql://<username:<password>@<id-address/hostname>/<database_name>'
SQLALCHEMY_DATAABASE_URL = 'postgresql://postgres:don\'tdothis@localhost/crud'
engine = create_engine(SQLALCHEMY_DATAABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Base.metadata.create_all(bind=engine)
