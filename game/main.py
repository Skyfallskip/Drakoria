#Loop principal
import pygame # Lib principal 
import sys
from core import mapa, database, uis  # Importa os libs personalizadas do jogo

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

# Loop Principal
def main():
    pygame.init()

    screen = pygame.display.set_mode((1280 ,720),)
    pygame.display.set_caption("Drakoria RPG")
    #pygame.display.set_icon()

    estado = "inicial"
    telas = {
        "inicial": TelaInicial(),
        "loading": TelaLoading(),
        "principal": TelaPrincipal()
    }

    clock = pygame.time.Clock()
    running = True

    while estado != 'sair':

        time_delta = clock.tick(60)/1000.0 # Controla o FPS do jogo

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = 'sair'

            uis.ui_manager.process_events(event)

        uis.ui_manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        uis.ui_manager.draw_ui(window_surface)

        pygame.display.update()

    pygame.quit()
    sys.exit()
# Fim

if __name__ == "__main__":
    main()
# Inicia o loop principal assim que o arquivo main.py é executado    