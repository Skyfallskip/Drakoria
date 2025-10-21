import pygame
from Core.Map_Renderer import render_maps
from Core.UIs_Handler import draw_game_ui
from Core.Buttons_Logic import Button
from Core.Map_Loader import load_world_maps


pygame.font.init()

# Testando as fontes externas
try:
        font_title = pygame.font.Font(r"Game\Assets\Font\Adventurer.ttf", 80)
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

BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

text_color,button_color = BLACK, ORANGE

# ----------------------------------------------------------------------------------------------------------------------------------------------------


def Main_Menu(screen, width, height):
        layers = [
                {"image": pygame.image.load(r"Game\Assets\Images\Main\version B\Layers\far-mountains.png").convert_alpha(), "speed": 0.1, "x": 0},
                {"image": pygame.image.load(r"Game\Assets\Images\Main\version B\Layers\sky.png").convert_alpha(), "speed": 0.2, "x": 0},
                {"image": pygame.image.load(r"Game\Assets\Images\Main\version B\Layers\middle-mountains.png").convert_alpha(), "speed": 0.4, "x": 0},
                {"image": pygame.image.load(r"Game\Assets\Images\Main\version B\Layers\myst.png").convert_alpha(), "speed": 0.6, "x": 0},
                {"image": pygame.image.load(r"Game\Assets\Images\Main\version B\Layers\far-trees.png").convert_alpha(), "speed": 0.8, "x": 0},
                {"image": pygame.image.load(r"Game\Assets\Images\Main\version B\Layers\near-trees.png").convert_alpha(), "speed": 1.2, "x": 0},
        ]

        for layer in layers:
                layer["image"] = pygame.transform.scale(layer["image"], (width, height)).convert_alpha()
        
        for layer in layers:
                screen.blit(layer["image"], (layer["x"], 0))
                screen.blit(layer["image"], (layer["x"] + width, 0))

        darker_surface = pygame.Surface((width // 2, height))
        darker_surface.set_alpha(128)  
        darker_surface.fill((0, 0, 0))

        screen.blit(darker_surface, (0, 0))
        
        title_shadow = font_title.render("DRAKORIA", True, text_color)
        screen.blit(title_shadow, (30, 72))

        title_text = font_title.render("DRAKORIA", True, (255, 255, 255))
        screen.blit(title_text, (25, 70))
        
        button_width = 200
        button_height = 60

        
        start_button = Button(30, (200+70), (button_width-60), button_height, "START",)
        settings_button = Button(30, (270+70), (button_width-5), button_height, "SETTINGS")
        exit_button = Button(20, (340+70), (button_width-70), button_height, "EXIT")
        
        start_button.draw(screen)
        settings_button.draw(screen)
        exit_button.draw(screen)
        
        return start_button, settings_button, exit_button


# View durante o jogo


# ----------------------------------------------------------------------------------------------------------------------------------------------------

selected_slot = None
slot_xx = 0
hotbar_y = 515
hotbar_x = 120

def Game_View(screen, width, height, maps, camera):
        global selected_slot, slot_xx,hotbar_x,hotbar_y
        selected_slot_highlight = pygame.image.load(r"Game\Assets\UIs\UI_Game\Hot_Bar\Selected_Item_Hot_Bar.png")

        # Renderiza os mapas
        render_maps(screen, maps, camera)

        # Desenha a UI do jogo
        draw_game_ui(screen, width, height)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                       pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()

                        # print(mouse_pos[0])
                        # print(mouse_pos[1])


                        #pygame.draw.rect(screen,BLACK,(20,340,50,55)) # debug (x,y,width,height)

                        for i in range(10):
                                        slot_x = hotbar_x + (i * 53)
                                        if (slot_x <= mouse_pos[0] <= slot_x + 53 and 
                                                hotbar_y <= mouse_pos[1] <= hotbar_y + 60):              
                                                print(f"Hotbar slot {i+1} clicked!")
                                                selected_slot = i+1
                                                slot_xx = slot_xx = hotbar_x + ((selected_slot-1) * 53)
                                                if i + 1 == 4:
                                                        slot_xx += 2
                                                elif i+ 1 == 5:
                                                        slot_xx +=4       
                                                elif i+ 1 == 6:
                                                        slot_xx +=5   
                                                elif i+ 1 == 7:
                                                        slot_xx +=6 
                                                elif i+ 1 == 8:
                                                        slot_xx +=7  
                                                elif i+ 1 == 9:
                                                        slot_xx +=8
                                                elif i+ 1 == 10:
                                                        slot_xx +=9                                                          

                        screen.blit(selected_slot_highlight,(slot_xx,(hotbar_y-3)))
                
                elif event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_1:
                                print("Hot bar 1")
                                selected_slot = 1
                                slot_xx = hotbar_x
                                

                        elif event.key == pygame.K_2:
                                print("Hot bar 2")
                                selected_slot = 2
                                slot_xx = hotbar_x + 53
                                

                        elif event.key == pygame.K_3:
                                print("Hot bar 3")
                                selected_slot = 3
                                slot_xx = (hotbar_x + ((selected_slot-1) * 53))
                                print(slot_xx)

                        elif event.key == pygame.K_4:
                                print("Hot bar 4")
                                selected_slot = 4
                                slot_xx = (hotbar_x + ((selected_slot-1) * 53)) + 2
                                print(slot_xx)

                        elif event.key == pygame.K_5:
                                print("Hot bar 5")
                                selected_slot = 5
                                slot_xx = hotbar_x + ((selected_slot-1) * 53) + 4
                                print(slot_xx)

                        elif event.key == pygame.K_6:
                                print("Hot bar 6")
                                selected_slot = 6
                                slot_xx = hotbar_x + ((selected_slot-1) * 53) + 5
                                print(slot_xx)

                        elif event.key == pygame.K_7:
                                print("Hot bar 7")
                                selected_slot = 7
                                slot_xx = hotbar_x + ((selected_slot-1) * 53) + 6
                                print(slot_xx)

                        elif event.key == pygame.K_8:
                                print("Hot bar 8")  
                                selected_slot = 8
                                slot_xx = hotbar_x + ((selected_slot-1) * 53) + 7
                                print(slot_xx)

                        elif event.key == pygame.K_9:
                                print("Hot bar 9")
                                selected_slot = 9
                                slot_xx = hotbar_x + ((selected_slot-1) * 53) + 8
                                print(slot_xx)

                        elif event.key == pygame.K_0:
                                print("Hot bar 10")
                                selected_slot = 10
                                slot_xx = hotbar_x + ((selected_slot-1) * 53) + 9
                                print(slot_xx)

        screen.blit(selected_slot_highlight,(slot_xx,(hotbar_y-3)))
        
        


# ----------------------------------------------------------------------------------------------------------------------------------------------------


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
                                return 3 # Volta para o estado do jogo
                        
                        elif mouse_pos[0] >= 10 and mouse_pos[0] <= 171 and mouse_pos[1] >= 67 and mouse_pos[1] <= 94:
                                print("Clicou na aba de inventario")
                                return 4
                        
                        #(55, 179),(171, 179),(55, 207),(170, 205)
                        elif mouse_pos[0] >= 55 and mouse_pos[0] <= 171 and mouse_pos[1] >= 179 and mouse_pos[1] <= 207:
                                print("Clicou na aba de quests")
                                return 7
                        
                        #(68, 256),(170, 256),(68, 281),(170, 282)
                        elif mouse_pos[0] >= 68 and mouse_pos[0] <= 170 and mouse_pos[1] >= 256 and mouse_pos[1] <= 281:
                                print("Clicou nas configurações")
                                return 9

                        if mouse_pos:
                                pass

                        
                if event.type == pygame.QUIT:
                    pygame.quit()


# ----------------------------------------------------------------------------------------------------------------------------------------------------


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
                                return 3 # Volta para o estado do jogo
                        #(10, 67),(10, 94),(171, 94),(170, 67)

                        elif mouse_pos[0] >= 10 and mouse_pos[0] <= 171 and mouse_pos[1] >= 67 and mouse_pos[1] <= 94:
                                print("Clicou na aba de inventario")
                                return 4

                        #(55, 179),(171, 179),(55, 207),(170, 205)
                        elif mouse_pos[0] >= 55 and mouse_pos[0] <= 171 and mouse_pos[1] >= 179 and mouse_pos[1] <= 207:
                                print("Clicou na aba de quests")
                                return 7
                        
                        elif mouse_pos[0] >= 68 and mouse_pos[0] <= 170 and mouse_pos[1] >= 256 and mouse_pos[1] <= 281:
                                print("Clicou nas configurações")
                                return 9
                        
                if event.type == pygame.QUIT:
                    pygame.quit()



# ----------------------------------------------------------------------------------------------------------------------------------------------------



def Stats_View():
        pass


# ----------------------------------------------------------------------------------------------------------------------------------------------------

current_Setting = None

def Config_View(screen,mouse_pos,maps,camera):
                
        # Carregar fontes
        pygame.font.init()
        
        global current_Setting

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
                                        
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                        print(mouse_pos) # Debug da posição do mouse
                        # ------------ Book Tabs ------------

                        if mouse_pos[0] >= 750 and mouse_pos[0] <= 790 and mouse_pos[1] >= 30 and mouse_pos[1] <= 70:
                                pygame.draw.rect(screen,(255,0,0),(750,30,40,40),2) # debug (x,y,width,height)
                                print("Clicou no X")
                                return 3 # Volta para o estado do jogo
                        #(10, 67),(10, 94),(171, 94),(170, 67)

                        elif mouse_pos[0] >= 10 and mouse_pos[0] <= 171 and mouse_pos[1] >= 67 and mouse_pos[1] <= 94:
                                print("Clicou na aba de inventario")
                                return 4
                        
                        elif mouse_pos[0] >= 68 and mouse_pos[0] <= 170 and mouse_pos[1] >= 256 and mouse_pos[1] <= 281:
                                print("Clicou nas configurações")
                                return 9
                        
                        #(55, 179),(171, 179),(55, 207),(170, 205)
                        elif mouse_pos[0] >= 55 and mouse_pos[0] <= 171 and mouse_pos[1] >= 179 and mouse_pos[1] <= 207:
                                print("Clicou na aba de quests")
                                return 7
                        
                        # ------------ Settings Tabs ------------

                        # Not working fully yet
                        # (198, 69),(425, 69),(198, 99), (426, 100)
                        if mouse_pos[0] >= 198 and mouse_pos[0] <= 425 and mouse_pos[1] >= 69 and mouse_pos[1] <= 99:
                                print("Clicou na aba de Audio")
                                current_Setting = 0

                        
                        #(198, 109),(426, 109),(199, 140),(425, 139)
                        elif mouse_pos[0] >= 198 and mouse_pos[0] <= 426 and mouse_pos[1] >= 109 and mouse_pos[1] <= 139:
                                print("Clicou na aba de video")
                                current_Setting = 1

                        
                        #(199, 149),(424, 149),(426, 179),(199, 180)
                        elif mouse_pos[0] >= 199 and mouse_pos[0] <= 424 and mouse_pos[1] >= 149 and mouse_pos[1] <= 179:
                                print("Clicou na aba de controles")
                                current_Setting = 2

                        
                        #(199, 189),(426, 189),(199, 219),(425, 219)
                        elif mouse_pos[0] >= 199 and mouse_pos[0] <= 426 and mouse_pos[1] >= 189 and mouse_pos[1] <= 219:
                                print("Clicou na aba de creditos")
                                current_Setting = 3


        if current_Setting == 0:
                Audio_Config = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Config_Tab\Audio_Tab.png")
                Audio_Config = pygame.transform.scale(Audio_Config, (700,500))
                screen.blit(Audio_Config, (47, 35))

        elif current_Setting == 1:
                Video_Config = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Config_Tab\Video_Tab.png")
                Video_Config = pygame.transform.scale(Video_Config, (700,500))
                screen.blit(Video_Config, (47, 35))

        elif current_Setting == 2:
                Controls_Config = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Config_Tab\Controls_Tab.png")
                Controls_Config = pygame.transform.scale(Controls_Config, (700,500))
                screen.blit(Controls_Config, (47, 35))
        
        elif current_Setting == 3:
                Credits_Config = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Config_Tab\Credits_Tab.png")
                Credits_Config = pygame.transform.scale(Credits_Config, (700,500))
                screen.blit(Credits_Config, (47, 35))
                        

        

# ----------------------------------------------------------------------------------------------------------------------------------------------------


def Skills_View():
        pass

# ----------------------------------------------------------------------------------------------------------------------------------------------------


def Main_Menu_Settings_View():
        pass


# ----------------------------------------------------------------------------------------------------------------------------------------------------



def Account_Menu_View(screen,maps):
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

    #nao irei implementar nunca. Nem morto

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                if username_rect.collidepoint(event.pos):
                    active_input = "username"
                elif password_rect.collidepoint(event.pos):
                    active_input = "password"
                else:
                    active_input = None

                # Se estiver logado e usuario ja existir entra direto no map

                if login_button.is_clicked(event):
                        if username_text and password_text:
                                maps = load_world_maps(r"Tiled_Map_Editor_Stuff\World\Zones.world")
                                print("Loaded maps:", len(maps))
                                print(f"Username: {username_text}, Password: {password_text}")

                                return 3
                        print("Login clicked")
                        
                
                elif login_button.is_clicked(event):
                      print("Preencha todos os campos")

                # Se nao exister um usuario com esse username e senha e clicou em criar, pagina de escolher classe e rng da raça

                elif create_button.is_clicked(event) and username_text and password_text:
                        return 2

                
                elif back_button.is_clicked(event):
                    print("Back clicked")
                    return 0

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
                        maps = load_world_maps(r"Tiled_Map_Editor_Stuff\World\Zones.world")
                        print("Loaded maps:", len(maps))
                        print(f"Username: {username_text}, Password: {password_text}")
                        return [3,maps]
                    else:
                        if len(password_text) < 30:
                            password_text += event.unicode

        pygame.display.flip()
        clock.tick(60)


# ----------------------------------------------------------------------------------------------------------------------------------------------------

selected_class = None
highlighted = None
selected_row = None
selected_column = None

def Character_Selection_View(screen, mouse_pos):
        pygame.font.init()

        # --- BACKGROUND ---

        background = pygame.image.load(r"Game\Assets\Images\Main_Menu_Backgrond.png")
        background = pygame.transform.scale(background, (800, 600))
        screen.blit(background, (0, 0))

        # Menu 

        layer_1 = pygame.image.load(r"Game\Assets\UIs\Character_Selection\Layer_1.png")
        layer_1 = pygame.transform.scale(layer_1,(700,500))
        screen.blit(layer_1,(50,50))

        # Buttons

        Continue_button = Button(540, 480, 180, 50, "Continue", (210, 170, 140))
        Back_button = Button(80, 480, 180, 50, "Back", (210, 170, 140))

        Continue_button.draw(screen)
        Back_button.draw(screen)


        # Eventos

        global selected_class, selected_row, selected_column, highlighted

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                      pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                        #print(mouse_pos)
                
                        # Botoes de cada classe x,y

                        # Width 135 Height 130

                        # Warrior
                                # x 140 - 274 y 77 - 214 Fixed for first row

                        # Mage
                                # x 334 - 466 y 77 - 214 Fixed for first row

                        # Archer
                                # x 527 - 661 y 77 - 214 Fixed for first row

                        # Assassin
                                # x 140 - 274 , Y 237 - 374 Fixed for second row

                        # Priest        
                                # x 334 - 468 , Y 237 - 374 Fixed for second row

                        # Unknown
                                # x 527 - 661 , Y 237 - 374 Fixed for second row

                        #elif mouse_pos[0] >= 198 and mouse_pos[0] <= 426 and mouse_pos[1] >= 109 and mouse_pos[1] <= 139:
                        if mouse_pos[0] >= 140 and mouse_pos[0] <= 274 and mouse_pos[1] >= 77 and mouse_pos[1] <= 214:
                              #Colocoar um outline, salvar class selection como warrior... bla bla bla
                                print("Clicou em warrior")
                                selected_row = 1
                                selected_column = 1
                                selected_class = "Warrior"
                                highlighted = pygame.image.load(r"Game\Assets\UIs\Character_Selection\Selected_Warrior.png")
                        
                        elif mouse_pos[0] >= 334 and mouse_pos[0] <= 466 and mouse_pos[1] >= 77 and mouse_pos[1] <= 214:
                                selected_column = 2
                                selected_row = 1
                                selected_class = "Mage"
                                highlighted = pygame.image.load(r"Game\Assets\UIs\Character_Selection\Selected_Mage.png")

                                print("Clicou em mage")
                        
                        elif mouse_pos[0] >= 527 and mouse_pos[0] <= 661 and mouse_pos[1] >= 77 and mouse_pos[1] <= 214:
                                selected_row = 1
                                selected_class = "Archer"
                                selected_column = 3
                                highlighted = pygame.image.load(r"Game\Assets\UIs\Character_Selection\Selected_Archer.png")

                                print("Clicou em archer")

                        elif mouse_pos[0] >= 140 and mouse_pos[0] <= 274 and mouse_pos[1] >= 237 and mouse_pos[1] <= 374:
                                selected_column = 1
                                selected_row = 0
                                selected_class = "Assassin"
                                highlighted = pygame.image.load(r"Game\Assets\UIs\Character_Selection\Selected_Assassin.png")

                                print("Clicou em Assassin")

                        elif mouse_pos[0] >= 334 and mouse_pos[0] <= 466 and mouse_pos[1] >= 237 and mouse_pos[1] <= 374:
                                selected_row = 0
                                selected_column = 2
                                selected_class = "Priest"
                                highlighted = pygame.image.load(r"Game\Assets\UIs\Character_Selection\Selected_Priest.png")

                                print("Clicou em Priest")
                        
                        elif mouse_pos[0] >= 527 and mouse_pos[0] <= 661 and mouse_pos[1] >= 237 and mouse_pos[1] <= 374:
                                selected_row = 0
                                selected_column = 3
                                selected_class = "None"
                                highlighted = pygame.image.load(r"Game\Assets\UIs\Character_Selection\Selected_Unknown.png")
                                print("Clicou em Unknown")
                        
                        if Back_button.is_clicked(event):
                               return 1

                        if Continue_button.is_clicked(event) and selected_class:
                                print(selected_class)
                                return 2.5

                        elif Continue_button.is_clicked(event) and selected_class == None:
                                print(selected_class)
                                print("Escholha uma classe")


        if selected_row:
                if selected_column == 1:
                                screen.blit(highlighted,(140,77))
                elif selected_column == 2:
                                screen.blit(highlighted,(334,77))
                elif selected_column == 3:
                                screen.blit(highlighted,(527,77))
        else:
                if selected_column == 1:
                                screen.blit(highlighted,(140,237))
                elif selected_column == 2:
                                screen.blit(highlighted,(334,237))
                elif selected_column == 3:
                                screen.blit(highlighted,(527,237))



                        




def Character_Race_View(screen):
        pygame.font.init()

        background = pygame.image.load(r"Game\Assets\Images\Main_Menu_Backgrond.png")
        background = pygame.transform.scale(background, (800, 600))
        screen.blit(background, (0, 0))

        layer_1 = pygame.image.load(r"Game\Assets\UIs\Character_Race\Base.png")
        layer_1 = pygame.transform.scale(layer_1,(700,500))
        screen.blit(layer_1,(50,50))


        font_atribute_name = pygame.font.Font(r"Game\Assets\Font\Adventurer.ttf", 20)
        font_atribute_value = pygame.font.Font(r"Game\Assets\Font\Adventurer.ttf", 20)

        # Atributos base da classe

        health_text = font_atribute_name.render("Health:", True, (0,0,0))
        screen.blit(health_text, (102, 160))

        health_value = font_atribute_value.render("100", True, (0,0,0))
        screen.blit(health_value, (170, 160))

        Mana_text = font_atribute_name.render("Mana:", True, (0,0,0))
        screen.blit(Mana_text, (102, 200))

        Mana_value = font_atribute_value.render("100", True, (0,0,0))
        screen.blit(Mana_value, (170, 200))

        Stamina_text = font_atribute_name.render("Stamina:", True, (0,0,0))
        screen.blit(Stamina_text, (102, 240))

        Stamina_value = font_atribute_value.render("100", True, (0,0,0))
        screen.blit(Stamina_value, (180, 240))

        Strength_text = font_atribute_name.render("Strength:", True, (0,0,0))
        screen.blit(Strength_text, (102, 280))

        Strength_value = font_atribute_value.render("100", True, (0,0,0))
        screen.blit(Strength_value, (190, 280))

        Defesa_text = font_atribute_name.render("Defesa:", True, (0,0,0))
        screen.blit(Defesa_text, (102, 320))

        Defesa_value = font_atribute_value.render("100", True, (0,0,0))
        screen.blit(Defesa_value, (170, 320))

        Agility_text = font_atribute_name.render("Agility:", True, (0,0,0))
        screen.blit(Agility_text, (102, 360))

        Agility_value = font_atribute_value.render("100", True, (0,0,0))
        screen.blit(Agility_value, (170, 360))

        intelligence_text = font_atribute_name.render("Intelligence:", True, (0,0,0))
        screen.blit(intelligence_text, (102, 400))

        intelligence_value = font_atribute_value.render("100", True, (0,0,0))
        screen.blit(intelligence_value, (210, 400))

        # Fim

        # Detalhes da classe

        class_name_text = font_atribute_name.render("Class Name:", True, (0,0,0))
        screen.blit(class_name_text, (300, 160))

        class_name_value = font_atribute_value.render("Warrior", True, (0,0,0))
        screen.blit(class_name_value, (430, 160))

        class_weapon_text = font_atribute_name.render("Starting Weapon:", True, (0,0,0))
        screen.blit(class_weapon_text, (310, 200))

        class_weapon_value = font_atribute_value.render("Sword", True, (0,0,0))
        screen.blit(class_weapon_value, (490, 200))

        # fim


        font_title = pygame.font.Font(r"Game\Assets\Font\Adventurer.ttf", 50)
        title_text = font_title.render("Character Race", True, (0, 0, 0))
        screen.blit(title_text, (240, 85))

        Continue_button = Button(540, 480, 180, 50, "Continue", (210, 170, 140))
        Back_button = Button(80, 480, 180, 50, "Back", (210, 170, 140))

        Continue_button.draw(screen)
        Back_button.draw(screen)




        for event in pygame.event.get():
               
               if event.type == pygame.QUIT:
                      pygame.quit()

               if event.type == pygame.MOUSEBUTTONDOWN:         
                      
                      if Back_button.is_clicked(event):
                             return 2
                      
                      if Continue_button.is_clicked(event):
                             return 3
                             
        return "Lorem Ipsun"
                
        





