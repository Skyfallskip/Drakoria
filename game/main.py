#Loop principal
import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Drakoria RPG")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Limpa a tela com preto

        # Aqui você pode desenhar sprites, mapas, etc.

        pygame.display.flip()
        clock.tick(60)  # Limita a 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()