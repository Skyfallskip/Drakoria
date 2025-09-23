import arcade as arc

screen_width = 800
screen_height = 600
screen_title = "Drakoria"
#screen_icon = ''

Sprite_Pixel_Size = 32
Grid_Pixel_Size = 32
Player_Scaling = 1

#Fisica do jogo

Move_Speed = 5


# Menus fora do jogo

class Main_Menu_View(arc.View):
    pass

class Setup_View(arc.View):
    pass

# Menus dentro do jogo

class GameView(arc.View):
    pass

# Aba do menu de inventario
class Inventory_View(arc.View):
    pass

# Aba de status do inventario
class Inventory_Status_Tab_View(arc.View):
    pass

# Aba de equipamentos do inventario
class Inventory_Equipment_Tab_View(arc.View):
    pass

