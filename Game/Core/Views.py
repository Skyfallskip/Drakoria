import pygame
import os
from Core.Map_Renderer import render_maps
from Core.UIs_Handler import draw_game_ui
from Core.Buttons_Logic import Button

pygame.font.init()

# Testando as fontes externas
try:
        font_title = pygame.font.Font(r"Game\Assets\Font\Adventurer.ttf", 100)
        font_button = pygame.font.Font(r"Game\Assets\Font\Adventurer.ttf", 40)
        controls_font = pygame.font.Font(r"Game\Assets\Font\Adventurer.ttf", 30)
        font = pygame.font.Font(r"Game\Assets\Font\Adventurer.ttf", 40)
        graphics_font = pygame.font.Font(r"Game\Assets\Font\Adventurer.ttf", 30)
except:
        font_title = pygame.font.SysFont(None, 100)
        font_button = pygame.font.SysFont(None, 40)
        controls_font = pygame.font.SysFont(None, 30)
        font = pygame.font.SysFont(None, 40)
        graphics_font = pygame.font.SysFont(None, 30)

    
# View do menu principal

def Main_Menu(screen, width, height, text_color, button_color):
        # Plano de fundo

        background = pygame.image.load(r"Game\Assets\Images\Main_Menu_Backgrond.png")

        background = pygame.transform.scale(background, (width, height))
        screen.blit(background, (0, 0))

        # Titulo do jogo
        title_text = font_title.render("Drakoria", True, text_color)
        title_rect = title_text.get_rect(center=(width // 2, height // 4))
        screen.blit(title_text, title_rect)

        # Dimensões dos botões
        button_width = 150
        button_height = 50
        button_y = 500
        button_spacing = 50

        # Posições dos botões
        start_x = (width // 2) - button_width - button_spacing
        settings_x = width // 2
        exit_x = (width // 2) + button_width + button_spacing

        # Cria instâncias dos botões usando Buttons_Logic
        start_button = Button(start_x - button_width // 2, button_y, button_width, button_height, "Start", button_color)
        settings_button = Button(settings_x - button_width // 2, button_y, button_width, button_height, "Settings", button_color)
        exit_button = Button(exit_x - button_width // 2, button_y, button_width, button_height, "Exit", button_color)

        # Desenha os botões
        start_button.draw(screen)
        settings_button.draw(screen)
        exit_button.draw(screen)



        return start_button, settings_button, exit_button


# View durante o jogo

def Game_View(screen, width, height, maps, camera):
        # Renderiza os mapas
        render_maps(screen, maps, camera)

        # Desenha a UI do jogo
        draw_game_ui(screen, width, height)


def Backpack_View(screen,mouse_pos,maps,camera):

        # Carregar fontes
        pygame.font.init()

        render_maps(screen,maps,camera) # Deixa o mapa de fundo

        layer_1_Inventory = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Inventory_Tab\Layer_1.png")
        layer_1_Inventory = pygame.transform.scale(layer_1_Inventory, (800-32, 500))
        screen.blit(layer_1_Inventory, (0, 30))
        
        layer_4_Inventory = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Inventory_Tab\Layer_4.png")
        layer_4_Inventory = pygame.transform.scale(layer_4_Inventory, (250, 300))
        screen.blit(layer_4_Inventory, (190, 200))

        layer_5_Inventory = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Inventory_Tab\Layer_5.png")
        layer_5_Inventory = pygame.transform.scale(layer_5_Inventory, (250, 100))
        screen.blit(layer_5_Inventory, (190, 70))

        layer_6_Inventory = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Inventory_Tab\Layer_6.png")
        layer_6_Inventory = pygame.transform.scale(layer_6_Inventory, (280, 440))
        screen.blit(layer_6_Inventory, (465,60))

        layer_8_Inventory = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Inventory_Tab\Layer_8.png")
        layer_8_Inventory = pygame.transform.scale(layer_8_Inventory, (70, 70))
        screen.blit(layer_8_Inventory, (478, 78))

        layer_9_Inventory = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Inventory_Tab\Layer_9.png")
        layer_9_Inventory = pygame.transform.scale(layer_9_Inventory, (150, 70))
        screen.blit(layer_9_Inventory, (570, 78))

        # layer_10_Inventory = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Inventory_Tab\Layer_10.png")
        # layer_10_Inventory = pygame.transform.scale(layer_10_Inventory, (200, 50))  refazer
        # screen.blit(layer_10_Inventory, (0, 30))
        

def Quests_View():
        pass

def Stats_View():
        pass

def Settings_View():
        pass

def Skills_View():
        pass

def Character_Creation_View():
        pass

def Main_Menu_Settings_View():
        pass

