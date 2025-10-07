import pygame
from Camera_Handler import Camera
from Map_Loader import load_world_maps

class Player:
    def __init__(self, x, y, sprite_path):
        self.x = x
        self.y = y
        self.speed = 4
        self.sprite_sheet = pygame.image.load(sprite_path).convert_alpha()
        self.columns = 12
        self.rows = 8
        self.frame_width = self.sprite_sheet.get_width() // 12
        self.frame_height = self.sprite_sheet.get_height() // self.rows
        self.current_frame = 0
        self.current_row = 0  # 0: down, 1: left, 2: right, 3: up
        self.animation_timer = 0
        self.animation_speed = 0.12  # fps

    #Desenha o jogador na tela
    def draw(self, screen, camera):
        Camera.x, Camera.y = camera.apply(self.x, self.y)
        frame_rect = pygame.Rect(
            self.current_frame * self.frame_width, #Pega a largura do frame
            self.current_row * self.frame_height, #pega a altura do frame
            self.frame_width - 30,
            self.frame_height
        ) 
        screen_width, screen_height = 800, 600
        center_x = screen_width // 2 - self.frame_width // 2
        center_y = screen_height // 2 - self.frame_height // 2
        screen.blit(self.sprite_sheet, (center_x, center_y), frame_rect)


    #Função para encontrar o tile de spawn
    #Nao funciona
    def find_spawn_tile(maps):
        for m in maps:
            tmx = m["tmx"]
            for layer in tmx.visible_layers:
                if hasattr(layer, "tiles"):
                    for x, y, gid in layer.tiles():
                        props = tmx.get_tile_properties_by_gid(gid)
                        if props and props.get("Spawn") == True:
                            # Retorna a posicao em pixels
                            Player.x = x * tmx.tilewidth + m["x"] * tmx.tilewidth
                            Player.y = y * tmx.tileheight + m["y"] * tmx.tileheight
                            return x, y

#Carrega os mapas
maps = load_world_maps(r"Tiled_Map_Editor_Stuff\World\Zones.world")

#Encontra o tile de spawn
Player.find_spawn_tile(maps)

