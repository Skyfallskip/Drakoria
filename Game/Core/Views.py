# Views.py
import pygame

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

def Main_Menu(screen, width, height, bg_color, text_color, button_color, button_text_color):
    # Plano de fundo
    screen.fill(bg_color)

    # Titulo do jogo
    title_text = font_title.render("Drakoria", True, text_color)
    title_rect = title_text.get_rect(center=(width // 2, height // 4))
    screen.blit(title_text, title_rect)

    # Dimensões dos botões
    button_width = 150
    button_height = 50
    button_radius = 20
    button_y = height // 2
    button_spacing = 50

    # Posições dos botões
    start_x = (width // 2) - button_width - button_spacing
    settings_x = width // 2
    exit_x = (width // 2) + button_width + button_spacing

    # Desenha os botões (como retângulos arredondados)
    pygame.draw.rect(screen, button_color, (start_x - button_width // 2, button_y, button_width, button_height), border_radius=button_radius)
    pygame.draw.rect(screen, button_color, (settings_x - button_width // 2, button_y, button_width, button_height), border_radius=button_radius)
    pygame.draw.rect(screen, button_color, (exit_x - button_width // 2, button_y, button_width, button_height), border_radius=button_radius)

    # Textos dos botões
    font_button = pygame.font.Font("Game\\Assets\\Font\\Adventurer.ttf", 40)
    
    start_text = font_button.render("Start", True, button_text_color)
    start_rect = start_text.get_rect(center=(start_x, button_y + button_height // 2))
    screen.blit(start_text, start_rect)

    settings_text = font_button.render("Settings", True, button_text_color)
    settings_rect = settings_text.get_rect(center=(settings_x, button_y + button_height // 2))
    screen.blit(settings_text, settings_rect)

    exit_text = font_button.render("Exit", True, button_text_color)
    exit_rect = exit_text.get_rect(center=(exit_x, button_y + button_height // 2))
    screen.blit(exit_text, exit_rect)


# Views das outras telas (esboço inicial, não funcional)

# def draw_audio_menu(screen, width, height, bg_color, menu_bg_color, button_color, text_color):
#     # Fill background
#     screen.fill(bg_color)

#     # Sidebar
#     pygame.draw.rect(screen, menu_bg_color, (0, 0, 200, height))

#     # Back button (X)
#     pygame.draw.rect(screen, button_color, (600, 0, 200, 50), border_radius=10)
#     back_text = pygame.font.SysFont(None, 40).render("X", True, text_color)
#     back_rect = back_text.get_rect(center=(700, 25))
#     screen.blit(back_text, back_rect)

#     # Menu options

#     options = ["Audio", "Gráficos", "Idioma", "Controles", "Sobre", "Tutorial"]
#     for i, option in enumerate(options):
#         text = font.render(option, True, text_color)
#         text_rect = text.get_rect(center=(100, 50 + i * 100))
#         screen.blit(text, text_rect)

#     # Audio settings
#     audio_font = pygame.font.SysFont(None, 30)
#     audio_options = [
#         "Volume:",
#         "Volume de Fundo:",
#         "Música de Fundo:",
#         "Efeito Sonoro:"
#     ]
#     for i, option in enumerate(audio_options):
#         text = audio_font.render(option, True, text_color)
#         text_rect = text.get_rect(topleft=(250, 100 + i * 50))
#         screen.blit(text, text_rect)

# def draw_graphics_menu(screen, width, height, bg_color, menu_bg_color, button_color, text_color):
#     # Fill background
#     screen.fill(bg_color)

#     # Sidebar
#     pygame.draw.rect(screen, menu_bg_color, (0, 0, 200, height))

#     # Back button (X)
#     pygame.draw.rect(screen, button_color, (600, 0, 200, 50), border_radius=10)
#     back_text = pygame.font.SysFont(None, 40).render("X", True, text_color)
#     back_rect = back_text.get_rect(center=(700, 25))
#     screen.blit(back_text, back_rect)

#     # Menu options
#     options = ["Audio", "Gráficos", "Idioma", "Controles", "Sobre", "Tutorial"]
#     for i, option in enumerate(options):
#         text = font.render(option, True, text_color)
#         text_rect = text.get_rect(center=(100, 50 + i * 100))
#         screen.blit(text, text_rect)

#     # Graphics settings

#     graphics_options = [
#         "FPS:",
#         "Efeitos:"
#     ]
#     for i, option in enumerate(graphics_options):
#         text = graphics_font.render(option, True, text_color)
#         text_rect = text.get_rect(topleft=(250, 100 + i * 50))
#         screen.blit(text, text_rect)

# def draw_controls_menu(screen, width, height, bg_color, menu_bg_color, button_color, text_color):
#     # Fill background
#     screen.fill(bg_color)

#     # Sidebar
#     pygame.draw.rect(screen, menu_bg_color, (0, 0, 200, height))

#     # Back button (X)
#     pygame.draw.rect(screen, button_color, (600, 0, 200, 50), border_radius=10)
#     back_text = pygame.font.SysFont(None, 40).render("X", True, text_color)
#     back_rect = back_text.get_rect(center=(700, 25))
#     screen.blit(back_text, back_rect)

#     # Menu options
#     options = ["Audio", "Gráficos", "Idioma", "Controles", "Sobre", "Tutorial"]
#     for i, option in enumerate(options):
#         text = font.render(option, True, text_color)
#         text_rect = text.get_rect(center=(100, 50 + i * 100))
#         screen.blit(text, text_rect)

#     # Controls settings

#     controls_options = [
#         "Interagir:",
#         "Mochila:",
#         "Botão de poção rápida mana:",
#         "Botão de poção rápida vida:",
#         "Habilidade 1:",
#         "Habilidade 2:",
#         "Habilidade 3:"
#     ]
#     for i, option in enumerate(controls_options):
#         text = controls_font.render(option, True, text_color)
#         text_rect = text.get_rect(topleft=(250, 100 + i * 50))
#         screen.blit(text, text_rect)