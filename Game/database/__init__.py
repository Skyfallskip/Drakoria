from session import Base, engine
from models import *

#É aqui que a magica acontece

# Cria as tabelas
Base.metadata.create_all(bind=engine)

