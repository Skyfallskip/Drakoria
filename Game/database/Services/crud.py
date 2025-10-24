from sqlalchemy.orm import Session
from database.models import personagem, status, classe


def create_account(db: Session, username: str, password: str, sprite_path: str):
    """
    Cria uma nova conta de personagem no banco.
    """
    # Verifica se já existe um personagem com esse username
    existing = db.query(personagem).filter(personagem.username == username).first()
    if existing:
        return False, f"Usuário '{username}' já existe!"

    # Busca a classe padrão (ex: Warrior, Mage, etc)
    char_class = db.query(classe).filter(classe.name == sprite_path.split("\\")[-1].split("_")[1].replace(".png", "")).first()
    if not char_class:
        # Caso não encontre uma classe associada ao nome, use None (classe será nula)
        char_class = db.query(classe).filter(classe.name == "Warrior").first()  # fallback

    # Cria o personagem
    new_char = personagem(
        username=username,
        password=password,
        sprite_path=sprite_path,
        classe=char_class
    )

    db.add(new_char)
    db.commit()
    db.refresh(new_char)

    # Cria o status inicial
    new_status = status(personagem_id=new_char.id_Personagem)
    db.add(new_status)
    db.commit()
    db.refresh(new_status)

    return True, f"Conta '{username}' criada com sucesso!"


def get_character_by_username(db: Session, username: str):
    """
    Retorna um personagem pelo nome de usuário.
    """
    return db.query(personagem).filter(personagem.username == username).first()


def get_all_characters(db: Session):
    """
    Retorna todos os personagens cadastrados.
    """
    return db.query(personagem).all()


def get_character_status(db: Session, char_id: int):
    """
    Retorna o status associado a um personagem.
    """
    return db.query(status).filter(status.personagem_id == char_id).first()


def update_character_position(db: Session, char_id: int, x: float, y: float):
    """
    Atualiza a posição (x, y) do personagem.
    """
    char = db.query(personagem).filter(personagem.id_Personagem == char_id).first()
    if not char:
        return False, "Personagem não encontrado."

    char.x = x
    char.y = y
    db.commit()
    return True, "Posição atualizada com sucesso!"


def update_character_status(db: Session, char_id: int, **kwargs):
    """
    Atualiza os atributos do status do personagem.
    Exemplo: update_character_status(db, 1, xp=100, level=2)
    """
    char_status = db.query(status).filter(status.personagem_id == char_id).first()
    if not char_status:
        return False, "Status não encontrado."

    for key, value in kwargs.items():
        if hasattr(char_status, key):
            setattr(char_status, key, value)

    db.commit()
    return True, "Status atualizado com sucesso!"


def delete_character(db: Session, char_id: int):
    """
    Exclui um personagem e seu status.
    """
    char = db.query(personagem).filter(personagem.id_Personagem == char_id).first()
    if not char:
        return False, "Personagem não encontrado."

    # Deleta o status vinculado
    db.query(status).filter(status.personagem_id == char_id).delete()

    # Deleta o personagem
    db.delete(char)
    db.commit()
    return True, f"Personagem '{char.username}' deletado com sucesso!"