import pygame

class Camera:
    def __init__(self, screen_width, screen_height, x=0, y=0):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = x
        self.y = y

    def apply(self, target_x, target_y):

        self.x = target_x - self.screen_width // 2
        self.y = target_y - self.screen_height // 2
        return self.x, self.y

    def update(self, player):
        self.x, self.y = self.apply(player.x, player.y)

    def apply_rect(self, rect):

        return pygame.Rect((rect.x - self.x)-32, (rect.y - self.y)-15, rect.width, rect.height)

    def apply_pos(self, x, y):

        return (x - self.x, y - self.y)