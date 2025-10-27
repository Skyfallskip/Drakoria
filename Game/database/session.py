from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from database.models import *

DATABASE_URL = "sqlite:///drakoria.db"  

engine = create_engine(
    DATABASE_URL, 
    echo=False,       
    future=True
)

# Base = declarative_base()

Base.metadata.create_all(bind=engine)

# inspector = inspect(engine)
# tables = inspector.get_table_names()
# print("Tables:", tables)

SessionLocal = scoped_session(
    sessionmaker(bind=engine, autoflush=False, autocommit=False)
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
