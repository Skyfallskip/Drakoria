import json
import os
from pytmx import load_pygame
import pygame

def load_world_maps(world_file):
    with open(world_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    loaded_maps = []
    collision_rects = []
    base_dir = os.path.dirname(world_file)  # pega a pasta do .world

    for m in data["maps"]:
        # Normaliza o caminho relativo
        map_path = os.path.normpath(os.path.join(base_dir, m["fileName"]))
        
        # Carrega o TMX
        tmx_data = load_pygame(map_path)
        
        if "collision" in tmx_data.layernames:
            collision_layer = tmx_data.get_layer_by_name("collision")
            for obj in collision_layer:
                if hasattr(obj, 'x') and hasattr(obj, 'y') and hasattr(obj, 'width') and hasattr(obj, 'height'):
                    rect = pygame.Rect(obj.x + m["x"], obj.y + m["y"], obj.width, obj.height)
                    collision_rects.append(rect)

        loaded_maps.append({
            "tmx": tmx_data,
            "x": m["x"],
            "y": m["y"]
        })

    return [loaded_maps,collision_rects]