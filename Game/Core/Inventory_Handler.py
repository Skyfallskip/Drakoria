import pygame
from Game.main import mouse_pos,screen

class inventory_page:

    def __init__(self,selected_slot):
        self.slots_page = 19
        self.mouse_pos = mouse_pos
        self.selected_slot = selected_slot

    
    def highlight_selected_slot(seletected_slot):
        highlighted_slot = pygame.image.load(r"Game\Assets\UIs\Book_Tabs\Inventory_Tab\Highlighted_slot.png")

#           x    y
#         (197, 206)
#         (244, 206)
#         (196, 257)
#         (244, 257)
# Cada slot tem 13x13
        slot = 13

        for i in range(4):
            slot_x = 197 + (i*10)
            if (slot_x <= mouse_pos[0] <= slot_x + 13) and (slot_y <= mouse_pos[1] <= slot_y + 13):
                screen.blit(highlighted_slot,(slot_x,slot_y))
                
            for j in range (5):
                slot_y = 257 + (j*10)
