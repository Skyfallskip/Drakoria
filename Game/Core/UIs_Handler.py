import pygame
import os

def load_ui_images():
    ui_path = "Game/Assets/UIs/UI_Game"
    # Carrega todas as imagens necessárias para a UI
    images = {
        "hotbar_holder": pygame.image.load(os.path.join(ui_path, "Hot_Bar", "Item_Frame_Holder_Hot_Bar1.png")),
        "hotbar_item": pygame.image.load(os.path.join(ui_path, "Hot_Bar", "Item_Frame_Hot_Bar1.png")),
        "minimap_layer1": pygame.image.load(os.path.join(ui_path, "Mini_Map", "Layer_1.png")),
        "minimap_layer2": pygame.image.load(os.path.join(ui_path, "Mini_Map", "Layer_2.png")),
        "backpack_slot": pygame.image.load(os.path.join(ui_path, "Side_Bar", "BackPack_Slot.png")),
        "gear_slot": pygame.image.load(os.path.join(ui_path, "Side_Bar", "Gear_Slot.png")),
        "gold_coin": pygame.image.load(os.path.join(ui_path, "Side_Bar", "Gold_Coin.png")),
        "quest_scroll": pygame.image.load(os.path.join(ui_path, "Side_Bar", "Quest_Scroll.png")),
        "health_bar": pygame.image.load(os.path.join(ui_path, "Profile", "Health_Bar_Profile_UI1.png")),
        "mana_bar": pygame.image.load(os.path.join(ui_path, "Profile", "Mana_Bar_Profile_UI1.png")),
        "stamina_bar": pygame.image.load(os.path.join(ui_path, "Profile", "Stamina_Bar_Profile_UI1.png")),
        "level_frame": pygame.image.load(os.path.join(ui_path, "Profile", "Level_Frame_Profile_UI1.png")),
        "level_bg": pygame.image.load(os.path.join(ui_path, "Profile", "Level_Frame_Background_Profile_UI1.png")),
        "level_number": pygame.image.load(os.path.join(ui_path, "Profile", "Level_Number_Profile_UI1.png")),
    }
    return images

def draw_game_ui(screen, width, height, images):
    # Perfil do jogador (topo esquerdo)
    profile_x = 20
    profile_y = 20
    screen.blit(images["level_bg"], (profile_x, profile_y))
    screen.blit(images["level_frame"], (profile_x, profile_y))
    screen.blit(images["level_number"], (profile_x, profile_y))

    # Barras ao lado
    bar_x = profile_x
    bar_y = profile_y
    screen.blit(images["health_bar"], (bar_x, bar_y))
    screen.blit(images["mana_bar"], (bar_x, bar_y))
    screen.blit(images["stamina_bar"], (bar_x, bar_y))

    # Ouro (baixo do perfil)
    gold_x = 20
    gold_y = profile_y + images["level_bg"].get_height() + 15
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

    # Mini mapa (topo direito)
    minimap_x = width - images["minimap_layer1"].get_width() - 20
    minimap_y = 20
    screen.blit(images["minimap_layer1"], (minimap_x, minimap_y))
    screen.blit(images["minimap_layer2"], (minimap_x, minimap_y))

    mini_map_font = pygame.font.Font("Game/Assets/Font/Adventurer.ttf", 18)
    mini_map_text = mini_map_font.render("Mini Mapa", True, (0, 0, 0))
    screen.blit(mini_map_text, (minimap_x + 10, minimap_y + 10))

    # Hotbar (centro inferior)
    hotbar_y = height - images["hotbar_holder"].get_height() - 20
    hotbar_x = (width - images["hotbar_holder"].get_width()) // 2
    screen.blit(images["hotbar_holder"], (hotbar_x, hotbar_y))

    screen.blit(images["hotbar_item"], (hotbar_x, hotbar_y))