from sqlalchemy.orm import Session
from database.models import personagem, status, classe

# Remove this line - you can't use Session class directly as a session instance
# db = Session

def create_personagem(db: Session, username: str, password: str, sprite_path: str):
    """
    Cria uma nova conta de personagem no banco.
    """
    # Verifica se já existe um personagem com esse username
    existing = db.query(personagem).filter(personagem.username == username).first()
    if existing:
        return False, f"Usuário '{username}' já existe!"

    # Busca a classe padrão (ex: Warrior, Mage, etc)
    # Extract class name from sprite path more safely
    try:
        class_name = sprite_path.split("\\")[-1].split("_")[0]  # Get "Warrior" from "Warrior_SpriteSheet.png"
        personagem_class = db.query(classe).filter(classe.name == class_name).first()
    except (IndexError, AttributeError):
        personagem_class = None
    
    if not personagem_class:
        # Caso não encontre uma classe associada ao nome, use Warrior como fallback
        personagem_class = db.query(classe).filter(classe.name == "Warrior").first()

    # Cria o personagem
    new_personagem = personagem(
        username=username,
        password=password,
        sprite_path=sprite_path,
        classe=personagem_class
    )

    db.add(new_personagem)
    db.commit()
    db.refresh(new_personagem)

    # Cria o status inicial
    new_status = status(personagem_id=new_personagem.id_Personagem)
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


def get_character_status(db: Session, id_Personagem: int):
    """
    Retorna o status associado a um personagem.
    """
    return db.query(status).filter(status.personagem_id == id_Personagem).first()


def update_character_position(db: Session, id_Personagem: int, x: float, y: float):
    """
    Atualiza a posição (x, y) do personagem.
    """
    char = db.query(personagem).filter(personagem.id_Personagem == id_Personagem).first()
    if not char:
        return False, "Personagem não encontrado."

    char.x = x
    char.y = y
    db.commit()
    return True, "Posição atualizada com sucesso!"


def update_character_status(db: Session, id_Personagem: int, **kwargs):
    """
    Atualiza os atributos do status do personagem.
    Exemplo: update_character_status(db, 1, xp=100, level=2)
    """
    char_status = db.query(status).filter(status.personagem_id == id_Personagem).first()
    if not char_status:
        return False, "Status não encontrado."

    for key, value in kwargs.items():
        if hasattr(char_status, key):
            setattr(char_status, key, value)

    db.commit()
    return True, "Status atualizado com sucesso!"


def delete_personagem(db: Session, id_Personagem: int):
    """
    Exclui um personagem e seu status.
    """
    char = db.query(personagem).filter(personagem.id_Personagem == id_Personagem).first()
    if not char:
        return False, "Personagem não encontrado."

    # Deleta o status vinculado
    db.query(status).filter(status.personagem_id == id_Personagem).delete()

    # Deleta o personagem
    db.delete(char)
    db.commit()
    return True, f"Personagem '{char.username}' deletado com sucesso!"


def get_status_personagem(db: Session, id_Personagem: int):
    """
    Retorna o status do personagem para atualizar as barras de health, mana e stamina.
    """
    char_status = db.query(status).filter(status.personagem_id == id_Personagem).first()
    
    if not char_status:
        return None
    
    # Calculate max values based on level and attributes
    max_health = 100 + (char_status.level * 10) + (char_status.defense * 5)
    max_mana = 100 + (char_status.level * 8) + (char_status.intelligence * 6)
    max_stamina = 100 + (char_status.level * 7) + (char_status.strength * 3)
    
    return {
        "current_health": char_status.health,
        "current_mana": char_status.mana,
        "current_stamina": char_status.stamina,
        "max_health": max_health,
        "max_mana": max_mana,
        "max_stamina": max_stamina,
        "level": char_status.level,
        "gold": char_status.gold
    }

def get_id_Personagem_from_name(db: Session, username: str):
    """
    Retorna o ID do personagem baseado no nome de usuário.
    """
    character = db.query(personagem).filter(personagem.username == username).first()
    
    if character:
        return character.id_Personagem
    else:
        return None
    
def login_personagem(db: Session, username: str, password: str):
    """
    Verifica se as credenciais de login estão corretas.
    Retorna o personagem se o login for bem-sucedido, None caso contrário.
    """
    # Busca o personagem pelo username
    character = db.query(personagem).filter(personagem.username == username).first()
    
    if not character:
        return None, "Usuário não encontrado!"
    
    if character.password != password:
        return None, "Senha incorreta!"
    
    return character, "Login bem-sucedido!"