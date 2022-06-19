from contextlib import contextmanager
from json import load
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

ENV = 'prod'

if ENV == 'dev':
    DATABASE_URL = os.getenv('DATABASE_URL')
else:
    DATABASE_URL = os.environ['DATABASE_URL']
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    print(DATABASE_URL)


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """FastAPI db session dependency."""

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@contextmanager
def get_session():
    """Db session for use out of FastAPI dependencies."""

    return get_db()