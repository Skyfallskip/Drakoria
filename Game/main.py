import pygame
from Core.Views import Main_Menu, Game_View
from Core.Player_Handler import Player
from Core.Map_Loader import load_world_maps
from Core.Camera_Handler import Camera
from Core.Movement_Handler import handle_player_movement


# Inicializa o pygame
pygame.init()

# Configura a tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Drakoria")

# Cores
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

STATE_MAIN_MENU = 1
STATE_GAME_RUNNING = 2
STATE_SETTINGS_MENU = 6

game_state = STATE_MAIN_MENU

player = Player(r"Game/Assets/Sprites/Characters/Warrior/Warrior_Sprite_Sheet.png")
camera = Camera(screen_width, screen_height, 0, 0)
maps = None  # Carrega os mapas apenas quando o jogo começa

# Loop principal do pygame
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(GRAY)  # Limpa a tela

    # Desenha o menu ou o jogo a cada frame
    if game_state == STATE_MAIN_MENU:
        start_btn, settings_btn, exit_btn = Main_Menu(screen, screen_width, screen_height, BLACK, ORANGE)
   
    elif game_state == STATE_GAME_RUNNING:
        keys = pygame.key.get_pressed()
        if maps:
            Game_View(screen, screen_width, screen_height, maps, camera)
        dt = clock.get_time() / 1000
        handle_player_movement(player, keys, dt)
        
        camera.update(player)

        player.draw(screen, camera)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == STATE_MAIN_MENU:
            if start_btn.is_clicked(event):
                # Carrega os mapas quando o jogo começa
                maps = load_world_maps(r"Tiled_Map_Editor_Stuff\World\Zones.world")
                print("Loaded maps:", len(maps))
                game_state = STATE_GAME_RUNNING
            elif settings_btn.is_clicked(event):
                game_state = STATE_SETTINGS_MENU
            elif exit_btn.is_clicked(event):
                running = False

        elif game_state == STATE_GAME_RUNNING:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                sidebar_x = 20
                sidebar_y = 95
                if sidebar_x <= mouse_pos[0] <= sidebar_x + 32 and sidebar_y <= mouse_pos[1] <= sidebar_y + 32:
                    print("Clicou na mochila")
                elif sidebar_x <= mouse_pos[0] <= sidebar_x + 32 and sidebar_y + 70 <= mouse_pos[1] <= sidebar_y + 70 + 32:
                    print("Clicou nas configurações")
                elif sidebar_x <= mouse_pos[0] <= sidebar_x + 32 and sidebar_y + 140 <= mouse_pos[1] <= sidebar_y + 140 + 32:
                    print("Clicou nas quests") 

                hotbar_y = 692
                hotbar_x = -53
                if hotbar_x <= mouse_pos[0] <= hotbar_x + 53 and hotbar_y <= mouse_pos[1] <= hotbar_y + 58:
                    print("Hotbar item clicked!")


    pygame.display.flip()
    clock.tick(60)  # Limita a 60 FPS

pygame.quit()