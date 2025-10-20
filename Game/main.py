import pygame
from Core.Views import *
from Core.Player_Handler import Player
from Core.Camera_Handler import Camera
from Core.Movement_Handler import handle_player_movement, Collision_Handler
from Core.Music_Handler import play_music, stop_music


# Inicializa os modules
pygame.init()
pygame.mixer.init()
menu_music_playing = False

# Configura a tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Drakoria")

icon = pygame.image.load(r"Game\Assets\Images\icon.png").convert_alpha()
pygame.display.set_icon(icon)

# Cores
GRAY = (128, 128, 128)

STATE_MAIN_MENU = 0
STATE_ACCOUNT_MENU = 1
STATE_CHARACTER_SELECTION = 2
STATE_CHARACTER_RACE = 2.5
STATE_GAME_RUNNING = 3
STATE_INVENTORY_OPEN = 4
STATE_STATUS_VIEW = 5
STATE_SKILLS_VIEW = 6
STATE_QUESTS_VIEW = 7
STATE_EQUIPMENT_VIEW = 8
STATE_CONFIG = 9
STATE_SETTINGS_MENU = 10

game_state = STATE_MAIN_MENU


player = Player(820,800,r"Game/Assets/Sprites/Characters/Mage/Mage_SpriteSheet.png")
camera = Camera(screen_width, screen_height, 0, 0)
maps = load_world_maps(r"Tiled_Map_Editor_Stuff\World\Zones.world")


# Loop principal do pygame
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(GRAY)  # Limpa a tela
    mouse_pos = pygame.mouse.get_pos()


    # --------------- Estados do jogo ----------------

    if game_state == STATE_MAIN_MENU: 
        start_btn, settings_btn, exit_btn = Main_Menu(screen, screen_width, screen_height)
        play_music(str(game_state))
        


   
    elif game_state == STATE_GAME_RUNNING:
        keys = pygame.key.get_pressed()
        stop_music()

        if maps:
            Game_View(screen, screen_width, screen_height, maps, camera)

        dt = clock.get_time() / 1000

        dx, dy = handle_player_movement(player, keys, dt)
        Collision_Handler(player,maps,dx,dy,screen,camera)
        
        camera.update(player)

        player.draw(screen, camera)

    # -------------------------------------------------
    
    elif game_state == STATE_ACCOUNT_MENU:
        Current_State = Account_Menu_View(screen, mouse_pos,map)
        stop_music()

        if Current_State == STATE_GAME_RUNNING:
            game_state = STATE_GAME_RUNNING
        
        elif Current_State == STATE_MAIN_MENU:
            game_state = STATE_MAIN_MENU

        elif Current_State == STATE_CHARACTER_SELECTION:
            game_state = STATE_CHARACTER_SELECTION

    # -------------------------------------------------

    
    elif game_state == STATE_CHARACTER_SELECTION:
        Current_State = Character_Selection_View(screen,mouse_pos)
        stop_music()

        #Escolheu a classe e clicou em continuar
        if Current_State == STATE_CHARACTER_RACE:
            game_state = STATE_CHARACTER_RACE
            Current_State = Character_Race_View(screen)

        #Clicou em Back
        elif Current_State == STATE_ACCOUNT_MENU:
            game_state = STATE_ACCOUNT_MENU

    # -------------------------------------------------


    elif game_state == STATE_CHARACTER_RACE:
        Current_State = Character_Race_View(screen)
        stop_music()

        #Clicou em continuar
        if Current_State == STATE_GAME_RUNNING:
            game_state = STATE_GAME_RUNNING
        
        #Clicou em back
        elif Current_State == STATE_CHARACTER_SELECTION:
            game_state = STATE_CHARACTER_SELECTION

    # -------------------------------------------------


    elif game_state == STATE_INVENTORY_OPEN:
        Current_State = Backpack_View(screen,mouse_pos,maps,camera)
        stop_music()

        #Fecha o inventario
        if Current_State == STATE_GAME_RUNNING:
            game_state = STATE_GAME_RUNNING

        #Muda pra aba de quests
        elif Current_State == STATE_QUESTS_VIEW:
            game_state = STATE_QUESTS_VIEW

        #Muda pra aba de configurações
        elif Current_State == STATE_CONFIG:
            game_state = STATE_CONFIG
        
    # -------------------------------------------------


    elif game_state == STATE_STATUS_VIEW:
         stop_music()
         pass
    
    # -------------------------------------------------


    elif game_state == STATE_SKILLS_VIEW:
         stop_music()
         pass
    
    # -------------------------------------------------

    
    elif game_state == STATE_QUESTS_VIEW:
        Current_State = Quests_View(screen,mouse_pos,maps,camera)
        stop_music()
        #Fecha a aba de quests
        if Current_State == STATE_GAME_RUNNING:
            game_state = STATE_GAME_RUNNING

        elif Current_State == STATE_INVENTORY_OPEN:
            game_state = STATE_INVENTORY_OPEN

        elif Current_State == STATE_CONFIG:
            game_state = STATE_CONFIG

    # -------------------------------------------------


    elif game_state == STATE_EQUIPMENT_VIEW:
        stop_music()
        pass

    # -------------------------------------------------


    elif game_state == STATE_CONFIG:
        Current_State = Config_View(screen,mouse_pos,maps,camera)
        stop_music()

        if Current_State == STATE_GAME_RUNNING:
            game_state = STATE_GAME_RUNNING

        elif Current_State == STATE_INVENTORY_OPEN:
            game_state = STATE_INVENTORY_OPEN

        elif Current_State == STATE_QUESTS_VIEW:
            game_state = STATE_QUESTS_VIEW

        elif Current_State == STATE_CONFIG:
            game_state = STATE_CONFIG

    # -------------------------------------------------

    # main menu config
    elif game_state == STATE_SETTINGS_MENU:
        stop_music()
        pass





    # --------------- Eventos ----------------

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == STATE_MAIN_MENU:
            if start_btn.is_clicked(event):
                game_state = STATE_ACCOUNT_MENU

            elif settings_btn.is_clicked(event):
                game_state = STATE_SETTINGS_MENU

            elif exit_btn.is_clicked(event):
                running = False

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
                    game_state = STATE_INVENTORY_OPEN
                    

                elif (sidebar_x <= mouse_pos[0] <= sidebar_x + sidebar_width and
                    (sidebar_y + sidebar_height) + 15 <= mouse_pos[1] <= sidebar_y + sidebar_height * 2):
                    game_state = STATE_CONFIG
                    print("Clicou nas configurações")

                elif (sidebar_x <= mouse_pos[0] <= sidebar_x + sidebar_width and
                    (sidebar_y + sidebar_height * 2) + 30 <= mouse_pos[1] <= (sidebar_y + sidebar_height * 3) + 30):
                    game_state = STATE_QUESTS_VIEW
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