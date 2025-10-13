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

        layer_10_1_Inventory = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Inventory_Tab\Layer_10-1.png")
        layer_10_1_Inventory = pygame.transform.scale(layer_10_1_Inventory, (200, 100)) 
        screen.blit(layer_10_1_Inventory, (380, 440))

        layer_10_2_Inventory = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Inventory_Tab\Layer_10-2.png")
        layer_10_2_Inventory = pygame.transform.scale(layer_10_2_Inventory, (300, 100)) 
        screen.blit(layer_10_2_Inventory, (465, 425))

        #Fechar e eventos
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        print(mouse_pos) # Debug da posição do mouse
                        if mouse_pos[0] >= 750 and mouse_pos[0] <= 790 and mouse_pos[1] >= 30 and mouse_pos[1] <= 70:
                                pygame.draw.rect(screen,(255,0,0),(750,30,40,40),2) # debug (x,y,width,height)
                                print("Clicou no X")
                                return 2 # Volta para o estado do jogo
                        
                        elif mouse_pos[0] >= 10 and mouse_pos[0] <= 171 and mouse_pos[1] >= 67 and mouse_pos[1] <= 94:
                                print("Clicou na aba de inventario")
                                return 3
                        
                        #(55, 179),(171, 179),(55, 207),(170, 205)
                        elif mouse_pos[0] >= 55 and mouse_pos[0] <= 171 and mouse_pos[1] >= 179 and mouse_pos[1] <= 207:
                                print("Clicou na aba de quests")
                                return 6
                        
                        #(68, 256),(170, 256),(68, 281),(170, 282)
                        elif mouse_pos[0] >= 68 and mouse_pos[0] <= 170 and mouse_pos[1] >= 256 and mouse_pos[1] <= 281:
                                print("Clicou nas configurações")
                                return 8

                        
                if event.type == pygame.QUIT:
                    pygame.quit()

def Quests_View(screen,mouse_pos,maps,camera):
        
        # Carregar fontes
        pygame.font.init()

        render_maps(screen,maps,camera) # Deixa o mapa de fundo

        layer_1_Quests = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Quest_Tab\Book_Quest.png")
        layer_1_Quests = pygame.transform.scale(layer_1_Quests, (800-32, 500))
        screen.blit(layer_1_Quests, (0, 30))

        layer_2_Quests = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Quest_Tab\Quest_Description_Holder.png")
        layer_2_Quests = pygame.transform.scale(layer_2_Quests, (750, 490))
        screen.blit(layer_2_Quests, (15, 30))

        layer_3_Quests = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Quest_Tab\Quest_Description.png")
        layer_3_Quests = pygame.transform.scale(layer_3_Quests, (750, 490))
        screen.blit(layer_3_Quests, (15, 30))

        # For quest in Personagem.quests:
        # Quest Card
        layer_4_Quests = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Quest_Tab\Quest_List_item.png")
        layer_4_Quests = pygame.transform.scale(layer_4_Quests, (810, 500))
        screen.blit(layer_4_Quests, (-19, 30))

        # If len(quests) > 8:
        # SrollBar
        layer_5_Quests = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Quest_Tab\Scroll_Bar_Quest.png")
        layer_5_Quests = pygame.transform.scale(layer_5_Quests, (600, 400))
        screen.blit(layer_5_Quests, (98, 37))

        #Fechar
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        #print(mouse_pos) # Debug da posição do mouse
                        if mouse_pos[0] >= 750 and mouse_pos[0] <= 790 and mouse_pos[1] >= 30 and mouse_pos[1] <= 70:
                                pygame.draw.rect(screen,(255,0,0),(750,30,40,40),2) # debug (x,y,width,height)
                                print("Clicou no X")
                                return 2 # Volta para o estado do jogo
                        #(10, 67),(10, 94),(171, 94),(170, 67)

                        elif mouse_pos[0] >= 10 and mouse_pos[0] <= 171 and mouse_pos[1] >= 67 and mouse_pos[1] <= 94:
                                print("Clicou na aba de inventario")
                                return 3

                        #(55, 179),(171, 179),(55, 207),(170, 205)
                        elif mouse_pos[0] >= 55 and mouse_pos[0] <= 171 and mouse_pos[1] >= 179 and mouse_pos[1] <= 207:
                                print("Clicou na aba de quests")
                                return 6
                        
                        elif mouse_pos[0] >= 68 and mouse_pos[0] <= 170 and mouse_pos[1] >= 256 and mouse_pos[1] <= 281:
                                print("Clicou nas configurações")
                                return 8
                        
                if event.type == pygame.QUIT:
                    pygame.quit()

        

def Stats_View():
        pass

def Config_View(screen,mouse_pos,maps,camera):
                
        # Carregar fontes
        pygame.font.init()
        current_Setting = 0

        render_maps(screen,maps,camera) # Deixa o mapa de fundo

        layer_1_Config = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Config_Tab\Book_Config.png")
        layer_1_Config = pygame.transform.scale(layer_1_Config, (800-32, 500))
        screen.blit(layer_1_Config, (0, 30))

        layer_2_Config = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Config_Tab\Config_Holder.png")
        layer_2_Config = pygame.transform.scale(layer_2_Config, (750, 490))
        screen.blit(layer_2_Config, (15, 30))

        layer_3_Config = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Config_Tab\Config_Holder.png")
        layer_3_Config = pygame.transform.scale(layer_3_Config, (750, 490))
        screen.blit(layer_3_Config, (-280, 30))

        layer_4_Config = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Config_Tab\Config_Sections_Buttons.png")
        layer_4_Config = pygame.transform.scale(layer_4_Config, (700,500))
        screen.blit(layer_4_Config, (25, 35))

        #Fechar
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:

                        print(mouse_pos) # Debug da posição do mouse
                        # ------------ Book Tabs ------------

                        if mouse_pos[0] >= 750 and mouse_pos[0] <= 790 and mouse_pos[1] >= 30 and mouse_pos[1] <= 70:
                                pygame.draw.rect(screen,(255,0,0),(750,30,40,40),2) # debug (x,y,width,height)
                                print("Clicou no X")
                                return 2 # Volta para o estado do jogo
                        #(10, 67),(10, 94),(171, 94),(170, 67)

                        elif mouse_pos[0] >= 10 and mouse_pos[0] <= 171 and mouse_pos[1] >= 67 and mouse_pos[1] <= 94:
                                print("Clicou na aba de inventario")
                                return 3
                        
                        elif mouse_pos[0] >= 68 and mouse_pos[0] <= 170 and mouse_pos[1] >= 256 and mouse_pos[1] <= 281:
                                print("Clicou nas configurações")
                                return 8
                        
                        #(55, 179),(171, 179),(55, 207),(170, 205)
                        elif mouse_pos[0] >= 55 and mouse_pos[0] <= 171 and mouse_pos[1] >= 179 and mouse_pos[1] <= 207:
                                print("Clicou na aba de quests")
                                return 6
                        
                        # ------------ Settings Tabs ------------

                        # Not working fully yet
                        # (198, 69),(425, 69),(198, 99), (426, 100)
                        if mouse_pos[0] >= 198 and mouse_pos[0] <= 425 and mouse_pos[1] >= 69 and mouse_pos[1] <= 99:
                                print("Clicou na aba de Audio")
                                current_Setting = 0
                                Audio_Config = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Config_Tab\Audio_Tab.png")
                                Audio_Config = pygame.transform.scale(Audio_Config, (700,500))
                                screen.blit(Audio_Config, (25, 35))
                        
                        #(198, 109),(426, 109),(199, 140),(425, 139)
                        elif mouse_pos[0] >= 198 and mouse_pos[0] <= 426 and mouse_pos[1] >= 109 and mouse_pos[1] <= 139:
                                print("Clicou na aba de video")
                                current_Setting = 1
                                Video_Config = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Config_Tab\Video_Tab.png")
                                Video_Config = pygame.transform.scale(Video_Config, (700,500))
                                screen.blit(Video_Config, (25, 35))
                        
                        #(199, 149),(424, 149),(426, 179),(199, 180)
                        elif mouse_pos[0] >= 199 and mouse_pos[0] <= 424 and mouse_pos[1] >= 149 and mouse_pos[1] <= 179:
                                print("Clicou na aba de controles")
                                current_Setting = 2
                                Controls_Config = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Config_Tab\Controls_Tab.png")
                                Controls_Config = pygame.transform.scale(Controls_Config, (700,500))
                                screen.blit(Controls_Config, (25, 35))
                        
                        #(199, 189),(426, 189),(199, 219),(425, 219)
                        elif mouse_pos[0] >= 199 and mouse_pos[0] <= 426 and mouse_pos[1] >= 189 and mouse_pos[1] <= 219:
                                print("Clicou na aba de creditos")
                                current_Setting = 3
                                Credits_Config = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Config_Tab\Credits_Tab.png")
                                Credits_Config = pygame.transform.scale(Credits_Config, (700,500))
                                screen.blit(Credits_Config, (25, 35))



                        

                        
                if event.type == pygame.QUIT:
                    pygame.quit()
        

def Skills_View():
        pass

def Character_Creation_View():
        pass

def Main_Menu_Settings_View():
        pass

import pygame
from Core.Buttons_Logic import Button

def Account_Menu_View(screen, mouse_pos):
    pygame.font.init()
    clock = pygame.time.Clock()

    # --- BACKGROUND ---
    background = pygame.image.load(r"Game\Assets\Images\Main_Menu_Backgrond.png")
    background = pygame.transform.scale(background, (800, 600))
    screen.blit(background, (0, 0))

    # Menu Principal
    layer_1 = pygame.image.load(r"Game\Assets\UIs\Account_Menu\Layer_1.png")
    layer_1 = pygame.transform.scale(layer_1, (700, 500))
    screen.blit(layer_1, (50, 50))

    # Fonts
    font_title = pygame.font.Font(r"Game\Assets\Font\Adventurer.ttf", 50)
    font_label = pygame.font.Font(r"Game\Assets\Font\Adventurer.ttf", 40)
    font_input = pygame.font.Font(r"Game\Assets\Font\Adventurer.ttf", 35)
    font_forgot = pygame.font.Font(r"Game\Assets\Font\Adventurer.ttf", 18)

    title_text = font_title.render("Account Center", True, (0, 0, 0))
    screen.blit(title_text, (240, 85))
    screen.blit(font_label.render("Username", True, (0, 0, 0)), (110, 150))
    screen.blit(font_label.render("Password", True, (0, 0, 0)), (110, 260))
    screen.blit(font_forgot.render("Esqueceu a Senha", True, (40, 30, 20)), (530, 360))

    # Input
    username_rect = pygame.Rect(90, 190, 630, 48)
    password_rect = pygame.Rect(90, 300, 630, 48)

    username_text = ""
    password_text = ""
    active_input = None
    cursor_visible = True
    cursor_timer = 0

    # Botoes
    login_button = Button(80, 430, 186, 76, "Log in", (210, 170, 140))
    create_button = Button(280, 430, 210, 76, "Create Acc", (210, 170, 140))
    back_button = Button(540, 430, 186, 76, "Back", (210, 170, 140))

    running = True
    while running:
        screen.blit(background, (0, 0))
        screen.blit(layer_1, (50, 50))
        screen.blit(title_text, (240, 85))
        screen.blit(font_label.render("Username", True, (0, 0, 0)), (110, 150))
        screen.blit(font_label.render("Password", True, (0, 0, 0)), (110, 260))
        screen.blit(font_forgot.render("Esqueceu a Senha", True, (40, 30, 20)), (530, 360))

        pygame.draw.rect(screen, (230, 216, 195, 10), username_rect, 0, 25)
        pygame.draw.rect(screen, (230, 216, 195, 10), password_rect, 0, 25)

        if not username_text and active_input != "username":
            screen.blit(font_input.render("Digite aqui", True, (90, 80, 70)), (120, 195))
        if not password_text and active_input != "password":
            screen.blit(font_input.render("Digite aqui", True, (90, 80, 70)), (120, 305))

        username_surface = font_input.render(username_text, True, (0, 0, 0))
        password_surface = font_input.render("*" * len(password_text), True, (0, 0, 0))

        screen.blit(username_surface, (120, 195))
        screen.blit(password_surface, (120, 305))

        cursor_timer += 1
        if cursor_timer >= 630:
            cursor_timer = 0
            cursor_visible = not cursor_visible

        if cursor_visible and active_input:
            cursor_x = 120 + font_input.size(username_text if active_input == "username" else "*" * len(password_text))[0] + 5
            cursor_y = 195 if active_input == "username" else 305
            pygame.draw.line(screen, (0, 0, 0), (cursor_x, cursor_y), (cursor_x, cursor_y + 40), 2)

        login_button.draw(screen)
        create_button.draw(screen)
        back_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 5

            if event.type == pygame.MOUSEBUTTONDOWN:
                if username_rect.collidepoint(event.pos):
                    active_input = "username"
                elif password_rect.collidepoint(event.pos):
                    active_input = "password"
                else:
                    active_input = None

                if login_button.is_clicked(event) and username_text and password_text:
                    print("Login clicked")
                    print(f"Username: {username_text}, Password: {password_text}")
                    return "Game_Running" #Temporario Retorna pro jogo so pra testa login
                elif login_button.is_clicked(event):
                      print("Preencha todos os campos")

                if create_button.is_clicked(event):
                    print("Create Account clicked")
                    return "Account_Creation"
                
                elif back_button.is_clicked(event):
                    print("Back clicked")
                    return "Main_Menu"

            if event.type == pygame.KEYDOWN:
                if active_input == "username":
                    if event.key == pygame.K_BACKSPACE:
                        username_text = username_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        active_input = "password"
                    else:
                        if len(username_text) < 30:
                            username_text += event.unicode

                elif active_input == "password":
                    if event.key == pygame.K_BACKSPACE:
                        password_text = password_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        print("Submitting login...")
                        return 1
                    else:
                        if len(password_text) < 30:
                            password_text += event.unicode

        pygame.display.flip()
        clock.tick(60)

    return 5


def Character_Selection_View(screen, mouse_pos):
        pass
