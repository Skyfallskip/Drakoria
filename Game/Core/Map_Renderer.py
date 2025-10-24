import pygame
import pytmx

#Renderiza os mapas na tela
def render_maps(screen, maps, camera):
    for m in maps[0]:
        tmx = m["tmx"]
        offset_x = m["x"] 
        offset_y = m["y"]

        for layer in tmx.visible_layers:
            if hasattr(layer, "tiles"):
                for x, y, gid in layer.tiles():
                    
                    # Se já veio como Surface
                    if isinstance(gid, pygame.Surface):
                        tile = gid
                    else:
                        tile = tmx.get_tile_image_by_gid(gid)

                    if tile:
                        screen.blit(tile,
                                     (
                                            x * tmx.tilewidth + offset_x - camera.x,
                                            y * tmx.tileheight + offset_y - camera.y
                                     ))

