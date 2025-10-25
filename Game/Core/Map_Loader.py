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
        print(f"Map offset: x={m['x']}, y={m['y']}")
        
        gids_with_collision = set()
        for gid in range(1, tmx_data.tilesets[0].firstgid + tmx_data.tilesets[0].tilecount):
            props = tmx_data.get_tile_properties_by_gid(gid)
            if props and props.get("Collision") == True:
                gids_with_collision.add(gid)
        
        print(f"GIDs with Collision=True: {gids_with_collision}")

        collision_count = 0
        
        for layer_num, layer in enumerate(tmx_data.visible_layers):
            if hasattr(layer, "data"):
                print(f"Checking layer {layer_num}: {layer.name}")
                for x in range(tmx_data.width):
                    for y in range(tmx_data.height):
                        gid = layer.data[y][x] if hasattr(layer.data, '__getitem__') and len(layer.data) > y else 0
                        
                        if gid != 0 and gid in gids_with_collision:
                            collision_count += 1
                            
                            world_x = x * 33 + (m["x"] + 1)
                            world_y = y * 32 + (m["y"] + 15)
                            
                            rect = pygame.Rect(world_x, world_y, 32, 32)
                            
                            #print(f"Collision tile at map coords ({x}, {y}) -> world coords ({world_x}, {world_y})")
                            
                            collision_rects.append([rect, i])

        #print(f"Collision tiles found in map {i}: {collision_count}")

        loaded_maps.append({
            "tmx": tmx_data,
            "x": m["x"],
            "y": m["y"],
            "width": tmx_data.width * 32,
            "height": tmx_data.height * 32
        })

    print(f"Loaded {len(loaded_maps)} maps with {len(collision_rects)} total collision rectangles.")
    
    # Debug: Print collision info per map
    for i in range(len(loaded_maps)):
        map_collisions = [rect for rect, map_idx in collision_rects if map_idx == i]
        print(f"Map {i} has {len(map_collisions)} collision rectangles")
        if map_collisions:
            first_collision = map_collisions[0]
            print(f"First collision rect: {first_collision}")
    
    return loaded_maps, collision_rects