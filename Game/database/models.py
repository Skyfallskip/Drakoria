from session import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, JSON

#Banco de dados sqlalchemy

#Tabelas do banco de dados

class personagem(Base):
    __tablename__ = "personagens"

    #Atributos base
    id_Personagem = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    idade = Column(Integer, nullable=False)
    genero = Column(String, nullable=False)
    perks = Column(JSON) # Lista em formato nome : Beneficio
    customizacao = Column(JSON)  # Exemplo: {"cabelo": "curto", etc} 

    # Relacionamentos 
    id_conta = Column(Integer, ForeignKey("Conta.id_Conta"))
    conta = relationship("Conta", back_populates="personagens")

    # id_trabalho = Column(Integer, ForeignKey("Trabalho.id_Trabalho"))
    # trabalho = relationship("Trabalho")

    status = relationship("status", uselist=False, back_populates="personagem")

    id_classe = Column(Integer, ForeignKey("Classe.id_Classe"))
    classe = relationship("Classe", back_populates="personagens")

    inventory = relationship("Inventory", uselist=False, back_populates="personagem")

    quests = relationship("Quest", secondary="Quest_Personagem", back_populates="personagens")

class inventory(Base):
    __tablename__ = "inventory"

    id_Inventory = Column(Integer, primary_key=True, index=True, autoincrement=True)
    items = Column(JSON)  # Dicionario de itens no inventario em formato nome : quantidade
    capacity = Column(Integer, default=100)  # Capacidade maxima do inventario

    personagem_id = Column(Integer, ForeignKey("personagens.id_Personagem"))
    personagem = relationship("Personagem", back_populates="inventory")

class status(Base):
    __tablename__ = "status"

    id_Status = Column(Integer, primary_key=True, index=True, autoincrement=True)
    health = Column(Float, default=100.0) #Hp
    mana = Column(Float, default=100.0) #Mp, usado para skills magicos
    stamina = Column(Float, default=100.0) #Sp, usado para skills fisicos
    strength = Column(Integer, default=10) #Str, Aumenta o dano fisico
    defense = Column(Integer, default=10) #Def, Aumenta a vida maxima
    agility = Column(Integer, default=10) #Agi, aumenta velocidade, esquiva, chance de acerto critico
    intelligence = Column(Integer, default=10) #Int, aumenta poder magico e mana maxima
    hunger = Column(Float, default=100.0) #Fome
    thirst = Column(Float, default=100.0) #Sede
    weight = Column(Float, default=0.0) #Peso atual
    max_weight = Column(Float, default=100.0) #Peso maximo

    xp = Column(Integer, default=0) #Experiencia
    level = Column(Integer, default=1) #Nivel
    gold = Column(Integer, default=0) #Ouro
    
    # Relacionamento um-para-um com Personagem

    personagem_id = Column(Integer, ForeignKey("personagens.id_Personagem"))
    personagem = relationship("Personagem", back_populates="status")


# Talvez remover
# class Trabalho(Base):
#     __tablename__ = "Trabalho"

#     id_Trabalho = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     name = Column(String, unique=True, nullable=False)
#     descricao = Column(String, nullable=False)
#     requisitos = Column(JSON)

class Conta(Base):
    __tablename__ = "Conta"

    id_Conta = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    personagens = relationship("Personagem", back_populates="conta")

class Quest(Base):
    __tablename__ = "Quest"

    id_Quest = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    descricao = Column(String, nullable=False)
    requisitos = Column(JSON)
    recompensas = Column(JSON)
    is_repeatable = Column(Boolean, default=False)
    Tipo = Column(String, nullable=False)  # Principal, Secundaria, etc

    personagens = relationship("Quest_Personagem", back_populates="quest")

class Quest_Personagem(Base):
    #Table associativa para o relacionamento muitos-para-muitos entre Personagem e Quest
    __tablename__ = "Quest_Personagem"

    id_Quest_Personagem = Column(Integer, primary_key=True, index=True, autoincrement=True)
    personagem_id = Column(Integer, ForeignKey("personagens.id_Personagem"))
    quest_id = Column(Integer, ForeignKey("Quest.id_Quest"))
    quest_status = Column(String, nullable=False)  # Ativa, Completa, Falhada

    personagem = relationship("Personagem", back_populates="quests")
    quest = relationship("Quest", back_populates="personagens")

class npc(Base):
    __tablename__ = "npc"

    id_NPC = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    role = Column(String, nullable=False)  # Ex: Vendedor, Guia, etc
    dialogue = Column(JSON) 
    sprite_path = Column(String, nullable=False)  # Exemplo: "sprites/npc1.png"

class classe(Base):
    __tablename__ = "classe"

    id_Classe = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    descricao = Column(String, nullable=False)
    habilidades = Column(JSON)  # Lista de habilidades especiais da classe
    bonus_atributos = Column(JSON)  # Atributos extras da classe, exemplo: {"mana_bonus": 50, "stamina_bonus": 20}
    buffs = Column(JSON)  # Buffs passivos da classe
    debuffs = Column(JSON)  # Debuffs passivos da classe
    requisitos = Column(JSON)  # Requisitos para escolher a classe, exemplo: {"level": 5, "strength": 15}
    
    personagens = relationship("Personagem", back_populates="classe")

class Monster(Base):
    __tablename__ = "Monster"

    id_Monster = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    loot = Column(JSON)  # Itens que o monstro pode dropar
    exp_reward = Column(Integer, default=50)  # Experiencia dada ao ser derrotado
    sprite_path = Column(String, nullable=False)  # Exemplo: "sprites/monster1.png"
    monster_type = Column(String, nullable=False)  # Ex: Animal, Humanoide, Demonio, etc
    spawn_cooldown = Column(Integer, default=300)  # Tempo em segundos para o monstro reaparecer
    Rank_monster = Column(String, nullable=False)  # Ex: Boss, Elite, Comum

    #Relacionamentos
    status = relationship("Status", uselist=False, back_populates="monster")
    id_status = Column(Integer, ForeignKey("Status.id_Status"))

    __mapper_args__ = {
        'polymorphic_identity': 'Monster',
        'polymorphic_on': Rank_monster
    }


class boss(Monster):
    __tablename__ = "boss"
    __mapper_args__ = {
        'polymorphic_identity': 'boss',
    }

    id_Boss = Column(Integer, ForeignKey("Monster.id_Monster"), primary_key=True)
    special_abilities = Column(JSON)  # Habilidades especiais do boss
    spawn_conditions = Column(JSON)  # Condições para o boss aparecer, exemplo: {"time": "night", "event": "eclipse"}

class item(Base):
    __tablename__ = "item"

    id_Item = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    item_type = Column(String, nullable=False)  # Ex: Consumivel, Equipamento, Material, etc
    description = Column(String, nullable=False)
    weight = Column(Integer, default=0)  # Peso do item
    value = Column(Integer, default=0)  # Valor em ouro
    rarity = Column(String, nullable=False)  # Comum, Incomum, Raro, Epico, Lendario, Mitico e Secreto
    attributes = Column(JSON)  # Atributos adicionais do item, exemplo: {"strength_bonus": 5}
    requirements = Column(JSON)  # Requisitos para usar o item, exemplo: {"level": 10, "class": "Guerreiro"}
    stackable = Column(Boolean, default=False)  # Se o item pode ser empilhado no inventario
    max_stack_size = Column(Integer, default=1)  # Tamanho maximo da pilha se for empilhavel
    sprite_path = Column(String, nullable=False)  # Exemplo: "assets/itens/item1.png"
    drop_chance = Column(Float, default=0.0)  # Chance de dropar o item de um monstro

    __mapper_args__ = {
        'polymorphic_identity': 'Item',
        'polymorphic_on': item_type
    }

class weapon(item):
    __tablename__ = "weapon"

    __mapper_args__ = {
        'polymorphic_identity': 'weapon',
    }

    id_Weapon = Column(Integer, ForeignKey("Item.id_Item"), primary_key=True)
    damage = Column(Float, nullable=False)  # Dano base da arma
    weapon_type = Column(String, nullable=False)  # Ex: Espada, Arco, Cajado, etc
    range_weapon = Column(Integer, default=1)  # Alcance da arma
    Classe_Weapon = Column(String, nullable=False)  # Classe que pode usar a arma
    attack_speed = Column(Float, default=1.0)  # Velocidade de ataque

class equipament(item):
    __tablename__ = "equipament"

    __mapper_args__ = {
        'polymorphic_identity': 'Equipament',
    }

    id_Equipament = Column(Integer, ForeignKey("Item.id_Item"), primary_key=True)
    equip_type = Column(String, nullable=False)  # Ex: Capacete, Peitoral, Botas, etc
    stat_bonus = Column(JSON)  # Bônus de status fornecidos pelo equipamento
    slot = Column(String, nullable=False)  # Slot onde o equipamento é usado, ex: cabeça, torso, pernas, etc
    Classe_Equipament = Column(String, nullable=False)  # Classe que pode usar o equipamento
    set_bonus = Column(JSON)  # Bônus de conjunto, exemplo: {"2 peças": {"strength_bonus": 5}, "4 peças": {"critical_chance": 10}}

class consumable(item):
    __tablename__ = "consumable"

    __mapper_args__ = {
        'polymorphic_identity': 'consumable',
    }

    id_Consumable = Column(Integer, ForeignKey("Item.id_Item"), primary_key=True)
    effect = Column(JSON)  # Efeito do consumível, exemplo: {"health_restore": 50}
    duration = Column(Integer, default=0)  # Duração do efeito em segundos, 0 se for instantâneo
    cooldown = Column(Integer, default=0)  # Tempo de recarga antes de poder usar novamente
    usable_in_combat = Column(Boolean, default=True)  # Se o consumível pode ser usado em combate

class skill(item):
    __tablename__ = "skill"

    __mapper_args__ = {
        'polymorphic_identity': 'skill',
    }

    id_Skill = Column(Integer, ForeignKey("Item.id_Item"), primary_key=True)
    cost = Column(Float, nullable=False)  # Custo de mana ou stamina para lançar a habilidade
    skill_type = Column(String, nullable=False)  # Ex: Ataque, Cura, Buff, Debuff, etc
    power = Column(Float, nullable=False)  # Poder da habilidade, pode ser dano ou cura
    cast_time = Column(Float, default=1.0)  # Tempo de conjuração em segundos
    cooldown = Column(Float, default=0.0)  # Tempo de recarga em segundos
    AOE = Column(Integer, default=1.0)  # Alcance da habilidade, Area of Effect
    Classe_Skill = Column(String, nullable=False)  # Classe que pode usar a habilidade
    element = Column(String, nullable=False)  # Elemento da habilidade, ex: Fogo, Gelo, Terra, etc