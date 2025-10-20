import pygame
#magia pura

class Button:
    def __init__(self, x, y, width, height, text, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(r"Game\Assets\Font\Adventurer.ttf", 36)
        self.color = color
        self.hover = False
        self.click_offset = 0
        
    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        self.hover = self.rect.collidepoint(mouse_pos)
        
        draw_rect = self.rect.copy()
        draw_rect.y += self.click_offset
        
        if self.color:
            if self.hover:
                button_color = tuple(min(c + 30, 255) for c in self.color)
                shadow_offset = 3
            else:
                button_color = self.color
                shadow_offset = 5
            
            shadow_color = tuple(max(c - 80, 0) for c in self.color)
            shadow_rect = draw_rect.copy()
            shadow_rect.y += shadow_offset
            pygame.draw.rect(screen, shadow_color, shadow_rect, border_radius=15)
            
            pygame.draw.rect(screen, button_color, draw_rect, border_radius=15)
            
            border_color = tuple(min(c + 50, 255) for c in button_color)
            pygame.draw.rect(screen, border_color, draw_rect, width=3, border_radius=15)
            
            inner_rect = draw_rect.inflate(-10, -10)
            inner_color = tuple(min(c + 20, 255) for c in button_color)
            pygame.draw.rect(screen, inner_color, inner_rect, width=2, border_radius=12)
            
            text_color = (255, 255, 255) if not self.hover else (255, 255, 200)
        else:
            base_text_color = (255, 255, 255)
            if self.hover:
                text_color = (255, 255, 200)
            else:
                text_color = base_text_color
        
        text_shadow = self.font.render(self.text, True, (0, 0, 0))
        shadow_rect = text_shadow.get_rect(center=(draw_rect.centerx + 2, draw_rect.centery + 2))
        screen.blit(text_shadow, shadow_rect)
        
        text_surf = self.font.render(self.text, True, text_color)
        text_rect = text_surf.get_rect(center=draw_rect.center)
        screen.blit(text_surf, text_rect)
        
        if self.click_offset > 0:
            self.click_offset = max(0, self.click_offset - 1)
    
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.click_offset = 3  # Button press effect
                return True
        return False
