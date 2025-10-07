import json
import os
from pytmx import load_pygame

def load_world_maps(world_file):
    with open(world_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    loaded_maps = []
    base_dir = os.path.dirname(world_file)  # pega a pasta do .world

    for m in data["maps"]:
        # Normaliza o caminho relativo
        map_path = os.path.normpath(os.path.join(base_dir, m["fileName"]))
        
        # Carrega o TMX
        tmx_data = load_pygame(map_path)
        
        loaded_maps.append({
            "tmx": tmx_data,
            "x": m["x"],
            "y": m["y"]
        })

    return loaded_maps