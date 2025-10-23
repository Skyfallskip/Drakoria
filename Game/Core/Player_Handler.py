import pygame

from Core.Camera_Handler import Camera

class Player:
    def __init__(self, x, y, sprite_path):
        self.x = x
        self.y = y
        self.speed = 4
        self.sprite_sheet = pygame.image.load(sprite_path).convert_alpha()
        self.columns = 6
        self.rows = 5
        self.frame_width = self.sprite_sheet.get_width() // 3
        self.frame_height = self.sprite_sheet.get_height() // self.rows

        self.current_frame = 0
        self.current_row = 0  # 0: down, 1: left, 2: right, 3: up
        self.animation_timer = 0
        self.animation_speed = 0.12  # fps

        self.frame = pygame.Rect(0, 0, self.frame_width, self.frame_height)
        self.player_rect = pygame.Rect(self.x, self.y, self.frame_width - 30, self.frame_height)

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

    def get_player_rect(self):
        self.player_rect.topleft = (self.x,self.y)
        return self.player_rect