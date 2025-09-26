import pygame
from Core.Views import Main_Menu

# Inicializa o pygame
pygame.init()

# Configura a tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Drakoria")

# Cores (Temporarias ate eu achar uma solução melhor)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
BROWN = (139, 69, 19)
WHITE = (255, 255, 255)

# Loop principal do pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Carrega a view do menu principal
    Main_Menu(screen, screen_width, screen_height, GRAY, BLACK, ORANGE, WHITE)

    pygame.display.flip()

# Sai do pygame
pygame.quit()