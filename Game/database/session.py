from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URL = "sqlite:///../drakoria.db"  # Troque para sua URL real do banco, ex: mysql+pymysql://user:pass@localhost/db

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))