from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    health = Column(Integer, default=100)
    # Adicione outros atributos conforme necessário