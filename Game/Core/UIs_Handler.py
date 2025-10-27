import pygame
import os
from database.Services import crud

ui_path = "Game/Assets/"
# Carrega todas as imagens necessárias para a UI
images = {

    #hotbar
    "hotbar_holder": pygame.image.load(os.path.join(ui_path,'UIs', 'UI_Game', "Hot_Bar", "Item_Frame_Holder_Hot_Bar1.png")),
    "hotbar_item": pygame.image.load(os.path.join(ui_path,'UIs','UI_Game', "Hot_Bar", "Item_Frame_Hot_Bar1.png")),

    #Side menu
    "backpack_slot": pygame.image.load(os.path.join(ui_path,'UIs', 'UI_Game', "Side_Bar", "BackPack_Slot.png")),
    "gear_slot": pygame.image.load(os.path.join(ui_path,'UIs', 'UI_Game', "Side_Bar", "Gear_Slot.png")),
    "quest_scroll": pygame.image.load(os.path.join(ui_path,'UIs', 'UI_Game', "Side_Bar", "Quest_Scroll.png")),
    "gold_coin": pygame.image.load(os.path.join(ui_path,'UIs', 'UI_Game', "Side_Bar", "Gold_Coin.png")),


    #Profile
    "health_bar": pygame.image.load(os.path.join(ui_path,'UIs', 'UI_Game', "Profile", "Health_Bar.png")),
    "mana_bar": pygame.image.load(os.path.join(ui_path,'UIs','UI_Game', "Profile", "Mana_Bar.png")),
    "stamina_bar": pygame.image.load(os.path.join(ui_path,'UIs', 'UI_Game', "Profile", "Stamina_Bar.png")),

    "level_frame": pygame.image.load(os.path.join(ui_path,'UIs', 'UI_Game', "Profile", "Level_Frame.png")), 
    "level_bg": pygame.image.load(os.path.join(ui_path,'UIs', 'UI_Game', "Profile", "Level_Frame_Background.png")), 
    "level_number": pygame.image.load(os.path.join(ui_path,'UIs','UI_Game', "Profile", "Level_Number.png")),


    }

profile_frame = images['level_frame']
profile_frame = pygame.transform.scale(profile_frame,(200,110))

profile_level = images['level_number']
profile_level = pygame.transform.scale(profile_level,(200,110))

profile_background = images['level_bg']
profile_background = pygame.transform.scale(profile_background,(200,110))


def draw_game_ui(screen, width, height, db, player_id):
    # Perfil do jogador (topo esquerdo)
    profile_x = 15
    profile_y = 30
    screen.blit(profile_background, (profile_x, profile_y))
    screen.blit(profile_frame, (profile_x, profile_y))
    screen.blit(profile_level, (profile_x, profile_y))

    # Barras ao lado
    bar_x = profile_x
    bar_y = profile_y

    health_percentage = 1.0
    mana_percentage = 1.0
    stamina_percentage = 1.0

    if player_id:
        status_info = crud.get_status_personagem(db, player_id)

        if status_info:
            # Calculate bar widths based on current values (assuming max is 100 for now)
            health_percentage = status_info["current_health"] / status_info["max_health"]
            mana_percentage = status_info["current_mana"] / status_info["max_mana"]
            stamina_percentage = status_info["current_stamina"] / status_info["max_stamina"]

        else:
            print(f"No status info found for player_id: {player_id}")
    
    else:
        print("No player_id provided, using default values")

    max_health = 115
    current_health = int(health_percentage * max_health)
    health_bg_rect = pygame.Rect((bar_x + 78), (bar_y + 16), current_health, 20)
    pygame.draw.rect(screen, (255, 0, 0), health_bg_rect)
    screen.blit(images["health_bar"].convert_alpha(), (bar_x, bar_y))

    max_mana = 89
    current_mana = int(mana_percentage * max_mana)
    mana_bg_rect = pygame.Rect((bar_x + 78), (bar_y + 42), current_mana, 18)
    pygame.draw.rect(screen, (0, 0, 255), mana_bg_rect)
    screen.blit(images["mana_bar"].convert_alpha(), (bar_x, bar_y))

    max_stamina = 66
    current_stamina = int(stamina_percentage * max_stamina)
    stamina_bg_rect = pygame.Rect((bar_x + 78), (bar_y + 65), current_stamina, 17)
    pygame.draw.rect(screen, (255, 255, 0), stamina_bg_rect)
    screen.blit(images["stamina_bar"].convert_alpha(), (bar_x, bar_y))


    # Ouro (baixo do perfil)
    gold_x = 20
    gold_y = 140
    screen.blit(images["gold_coin"], (gold_x, gold_y))

    gold_font = pygame.font.Font("Game/Assets/Font/Adventurer.ttf", 20)
    gold_text = gold_font.render("0", True, (0, 0, 0))
    screen.blit(gold_text, (gold_x + 40, gold_y + 10))

    # Side Bar (baixo do ouro)
    sidebar_x = 20
    sidebar_y = gold_y + 60
    screen.blit(images["backpack_slot"], (sidebar_x, sidebar_y))
    screen.blit(images["gear_slot"], (sidebar_x, sidebar_y + 70))
    screen.blit(images["quest_scroll"], (sidebar_x, sidebar_y + 140))

    # Hotbar (centro inferior)
    hotbar_y = height - images["hotbar_holder"].get_height() - 20
    hotbar_x = (width - images["hotbar_holder"].get_width()) // 2
    screen.blit(images["hotbar_holder"], (hotbar_x, hotbar_y))

    screen.blit(images["hotbar_item"], (hotbar_x, hotbar_y))
