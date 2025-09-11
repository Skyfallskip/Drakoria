#Loop principal
import pygame
import pyldtk
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Drakoria RPG")

    # Carregue o projeto LDtk
    project = pyldtk.LdtkProject("Drakoria_GitRepo/game/maps/Sample.ldtk")
    level = project.levels[0]  # Pega o primeiro nível

    # Exemplo: mostrar informações do nível
    print("Nome do nível:", level.identifier)
    print("Tamanho:", level.width, "x", level.height)
    print("Camadas:", [layer.identifier for layer in level.layer_instances])

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # Aqui você pode desenhar o mapa manualmente
        # Exemplo: desenhar tiles de uma camada
        # layer = level.layer_instances[0]
        # for tile in layer.grid_tiles:
        #     # Você precisa carregar o tileset e usar tile.src_x, tile.src_y, tile.px, tile.py
        #     pass

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()