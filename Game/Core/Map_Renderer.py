import pygame
import pytmx

def render_maps(screen, maps, camera):
    for m in maps:
        tmx = m["tmx"]
        offset_x = m["x"] * tmx.tilewidth
        offset_y = m["y"] * tmx.tileheight

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

