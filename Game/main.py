import pygame
from Core.Views import Main_Menu, Game_View, Backpack_View, Quests_View, Config_View,Account_Menu_View, Character_Selection_View
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

STATE_MAIN_MENU = "Main_Menu"
STATE_ACCOUNT_MENU = "Account_Menu"
STATE_CHARACTER_SELECTION = "Character_Selection"
STATE_GAME_RUNNING = "Game_Running"
STATE_INVENTORY_OPEN = "Inventory_Open"
STATE_STATUS_VIEW = "Status_View"
STATE_SKILLS_VIEW = "Skills_View"
STATE_QUESTS_VIEW = "Quests_View"
STATE_EQUIPMENT_VIEW = "Equipment_View"
STATE_CONFIG = "Config"
STATE_SETTINGS_MENU = "Settings_Menu"

game_state = STATE_MAIN_MENU

player = Player(820,800,r"Game/Assets/Sprites/Characters/Warrior/Warrior_Sprite_Sheet.png")
camera = Camera(screen_width, screen_height, 0, 0)
maps = None  # Carrega os mapas apenas quando o jogo começa

# Loop principal do pygame
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(GRAY)  # Limpa a tela
    mouse_pos = pygame.mouse.get_pos()


    # --------------- Estados do jogo ----------------

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
    
    elif game_state == STATE_ACCOUNT_MENU:
        Account_Menu_View(screen, mouse_pos)
    
    elif game_state == STATE_CHARACTER_SELECTION:
         pass
    
    elif game_state == STATE_INVENTORY_OPEN:
        Backpack_View(screen,mouse_pos,maps,camera)

        #Fecha o inventario
        if Backpack_View(screen,mouse_pos,maps,camera) == "Game_Running":
            game_state = STATE_GAME_RUNNING

        #Muda pra aba de quests
        elif Backpack_View(screen,mouse_pos,maps,camera) == "Quests_View":
            game_state = STATE_QUESTS_VIEW

        #Muda pra aba de configurações
        elif Backpack_View(screen,mouse_pos,maps,camera) == "Config":
            game_state = STATE_CONFIG
        
    elif game_state == STATE_STATUS_VIEW:
         pass
    
    elif game_state == STATE_SKILLS_VIEW:
         pass
    
    elif game_state == STATE_QUESTS_VIEW:
            Quests_View(screen,mouse_pos,maps,camera)
    
            #Fecha a aba de quests
            if Quests_View(screen,mouse_pos,maps,camera) == "Game_Running":
                game_state = STATE_GAME_RUNNING

            elif Quests_View(screen,mouse_pos,maps,camera) == "Inventory_Open":
                game_state = STATE_INVENTORY_OPEN

            elif Quests_View(screen,mouse_pos,maps,camera) == "Config":
                game_state = STATE_CONFIG

    elif game_state == STATE_EQUIPMENT_VIEW:
         pass

    # ingame config
    elif game_state == STATE_CONFIG:
        Config_View(screen,mouse_pos,maps,camera)

        if Config_View(screen,mouse_pos,maps,camera) == "Game_Running":
            game_state = STATE_GAME_RUNNING

        elif Config_View(screen,mouse_pos,maps,camera) == "Inventory_Open":
            game_state = STATE_INVENTORY_OPEN

        elif Config_View(screen,mouse_pos,maps,camera) == "Quests_View":
            game_state = STATE_QUESTS_VIEW

        elif Config_View(screen,mouse_pos,maps,camera) == "Config":
            game_state = STATE_CONFIG

    # main menu config
    elif game_state == STATE_SETTINGS_MENU:
         pass
    
    elif game_state == STATE_ACCOUNT_MENU:
        Account_Menu_View(screen, mouse_pos)

        if Account_Menu_View(screen, mouse_pos) == "Game_Running":
            game_state = STATE_GAME_RUNNING


    # --------------- Eventos ----------------

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == STATE_MAIN_MENU:
            if start_btn.is_clicked(event):
                game_state = STATE_ACCOUNT_MENU

                # Carrega os mapas quando o jogo começa
                # maps = load_world_maps(r"Tiled_Map_Editor_Stuff\World\Zones.world")
                # print("Loaded maps:", len(maps))
                # game_state = STATE_GAME_RUNNING

            elif settings_btn.is_clicked(event):
                game_state = STATE_SETTINGS_MENU

            elif exit_btn.is_clicked(event):
                running = False
        
        elif game_state == STATE_ACCOUNT_MENU:
            pass

        # Eventos durante o jogo
        #Funciona com sorte e com magica
        elif game_state == STATE_GAME_RUNNING:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                                
                # NAO MEXE NISSO AQUI PELO AMOR DE DEUS
                sidebar_x = 22
                sidebar_y = 200
                sidebar_width = 50   # largura do item
                sidebar_height = 55  # altura do item

                print(mouse_pos[0])
                print(mouse_pos[1])


                #pygame.draw.rect(screen,BLACK,(20,340,50,55)) # debug (x,y,width,height)
                if (sidebar_x <= mouse_pos[0] <= sidebar_x + sidebar_width and
                    sidebar_y <= mouse_pos[1] <= sidebar_y + sidebar_height):
                    print("Clicou na mochila")
                    game_state = 3
                    

                elif (sidebar_x <= mouse_pos[0] <= sidebar_x + sidebar_width and
                    (sidebar_y + sidebar_height) + 15 <= mouse_pos[1] <= sidebar_y + sidebar_height * 2):
                    game_state = 8
                    print("Clicou nas configurações")

                elif (sidebar_x <= mouse_pos[0] <= sidebar_x + sidebar_width and
                    (sidebar_y + sidebar_height * 2) + 30 <= mouse_pos[1] <= (sidebar_y + sidebar_height * 3) + 30):
                    game_state = 6
                    print("Clicou nas quests")


                hotbar_y = 515
                hotbar_x = 120
                for i in range(10):
                                slot_x = hotbar_x + (i * 53)
                                if (slot_x <= mouse_pos[0] <= slot_x + 53 and 
                                    hotbar_y <= mouse_pos[1] <= hotbar_y + 60):
                                    print(f"Hotbar slot {i+1} clicked!")
        

                 


    pygame.display.flip()
    clock.tick(60)  # Limita a 60 FPS

pygame.quit()