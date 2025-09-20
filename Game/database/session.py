from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

DATABASE_URL = "sqlite:///../drakoria.db"  

engine = create_engine(
    DATABASE_URL, 
    echo=True,       # Mostra os SQLs no terminal
    future=True
)

Base = declarative_base()

SessionLocal = scoped_session(
    sessionmaker(bind=engine, autoflush=False, autocommit=False)
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()