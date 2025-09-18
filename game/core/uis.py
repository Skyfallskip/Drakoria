import pygame_gui # Lib de interface grafica
from main.py import screen

ui_manager = pygame_gui.UIManager((1280, 720)) # Define o manager para trabalhar com a interface ( Mesmo valor da tela no main.py)

# Carregando temas

# ui_manager.load_theme('assets/UI/Tema.json')

ui_manager.load_theme('assets/UI/TelaLoading.json') # Carrega o tema da tela de loading

# Classes para cada tela

class Tela_Inicial:
    def run(self, screen):
        pass

class Tela_Loading:
    def run(self, screen):
        pass

class Tela_Principal:
    def run(self, screen):
        pass