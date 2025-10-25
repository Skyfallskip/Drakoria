import pygame

def handle_player_movement(player, keys, dt):

    dx, dy = 0, 0

    is_running = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
    movement_speed = player.speed + 4 if is_running else player.speed

    moved = False
    if keys[pygame.K_a]:
        dx -= movement_speed
        player.current_row = 3  # left
        moved = True
    elif keys[pygame.K_d]:
        dx += movement_speed
        player.current_row = 2  # right
        moved = True
    elif keys[pygame.K_w]:
        dy -= movement_speed
        player.current_row = 1  # up
        moved = True
    elif keys[pygame.K_s]:
        dy += movement_speed
        player.current_row = 0  # down
        moved = True

    if moved:
        player.animation_timer += dt
        if player.animation_timer >= player.animation_speed:

            player.current_frame = (player.current_frame + 1) % 3  # 3 frames por direção
            player.animation_timer = 0
    else:
        player.current_frame = 0  # Frame parado
    
    return dx, dy
    

def Collision_Handler(player, maps, dx, dy, screen=None, camera=None):
    player_rect = player.get_player_rect()
    loaded_maps = maps[0]
    collision_rects_with_map = maps[1]  # Lista de [rect, map_index] pares

    current_map_index = None
    for i, map_data in enumerate(loaded_maps):
        map_left = map_data["x"]
        map_top = map_data["y"]
        map_right = map_data["x"] + (map_data["tmx"].width * 32)
        map_bottom = map_data["y"] + (map_data["tmx"].height * 32)
        
        if (map_left <= player.x <= map_right and 
            map_top <= player.y <= map_bottom):
            current_map_index = i
            break

    if current_map_index is None:
        relevant_collisions = [rect for rect, map_idx in collision_rects_with_map]
    else:
        # So checa a colisão do mapa atual
        relevant_collisions = [rect for rect, map_idx in collision_rects_with_map if map_idx == current_map_index]

    #print(f"Player on map {current_map_index}, checking {len(relevant_collisions)} collision rects")

    if dx != 0:
        test_rect_x = player_rect.copy()
        test_rect_x.x += dx
        
        collision_x = False
        for obstacle in relevant_collisions:
            try:
                if test_rect_x.colliderect(obstacle):
                    if dx > 0:  # Moving right
                        player_rect.right = obstacle.left
                    elif dx < 0:  # Moving left
                        player_rect.left = obstacle.right
                    collision_x = True
                    break
            except TypeError as e:
                print(f"Error with collision rect: {obstacle}, error: {e}")
                continue
        
        if not collision_x:
            player_rect.x += dx

    if dy != 0:
        test_rect_y = player_rect.copy()
        test_rect_y.y += dy
        
        collision_y = False
        for obstacle in relevant_collisions:
            try:
                if test_rect_y.colliderect(obstacle):
                    if dy > 0:  # Moving down
                        player_rect.bottom = obstacle.top
                    elif dy < 0:  # Moving up
                        player_rect.top = obstacle.bottom
                    collision_y = True
                    break
            except TypeError as e:
                print(f"Error with collision rect: {obstacle}, error: {e}")
                continue
        
        if not collision_y:
            player_rect.y += dy

    player.x = player_rect.x
    player.y = player_rect.y

    # Debug: Draw collision rectangles (with camera offset)
    if screen and camera:
        # Draw player rect in green (convert to screen coordinates)
        screen_player_rect = camera.apply_rect(player_rect)
        pygame.draw.rect(screen, (0, 255, 0), screen_player_rect, 2)
        
        # Draw only relevant collision rects in red
        for obstacle in relevant_collisions:
            screen_obstacle_rect = camera.apply_rect(obstacle)

            if screen_obstacle_rect.colliderect(pygame.Rect(0, 0, camera.screen_width, camera.screen_height)):
                pygame.draw.rect(screen, (255, 0, 0), screen_obstacle_rect, 1)


    
    