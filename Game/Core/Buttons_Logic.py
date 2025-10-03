import pygame

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(r"Game\Assets\Font\Adventurer.ttf", 40)
        self.color = color

    #Desenha o botao
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=20)
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    #Verifica se o botao foi clicado
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False