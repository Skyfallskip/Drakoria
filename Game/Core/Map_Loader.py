import json
import os
from pytmx import load_pygame
import pygame

def load_world_maps(world_file):
    """
    Carrega os mapas apartir do JSON do mundo e funciona com sonhos e esperanças.
    """
    with open(world_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    loaded_maps = []
    collision_rects = []
    base_dir = os.path.dirname(world_file)


    for i, m in enumerate(data["maps"]):
        map_path = os.path.normpath(os.path.join(base_dir, m["fileName"]))
        tmx_data = load_pygame(map_path)
        
        print(f"\n--- Map {i + 1}: {m['fileName']} ---")
        
        gids_with_collision = set()
        for gid in range(1, tmx_data.tilesets[0].firstgid + tmx_data.tilesets[0].tilecount):
            props = tmx_data.get_tile_properties_by_gid(gid)
            if props and props.get("Collision") == True:
                gids_with_collision.add(gid)
        
        print(f"GIDs with Collision=True: {gids_with_collision}")

        collision_count = 0
        
        for layer in tmx_data.visible_layers:
            if hasattr(layer, "tiles"):
                for x in range(tmx_data.width):
                    for y in range(tmx_data.height):
                        gid = layer.data[x][y] 
                        
                        if gid != 0 and gid in gids_with_collision:
                            collision_count += 1
                            
                            rect = pygame.Rect(
                                x * 32  + m["x"],
                                y * 32 + m["y"],
                                32,
                                32
                            )
                            pygame.draw.rect(tmx_data.get_tile_image_by_gid(gid), (255, 0, 0), rect, 1)  # Debug: desenha o retângulo

                            collision_rects.append(rect)

        print(f"Collision tiles found: {collision_count}")

        loaded_maps.append({
            "tmx": tmx_data,
            "x": m["x"],
            "y": m["y"]
        })

    print(f"Loaded {len(loaded_maps)} maps with {len(collision_rects)} collision rectangles.")
    return loaded_maps, collision_rects