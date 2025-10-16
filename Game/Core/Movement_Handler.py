import pygame

def handle_player_movement(player, keys, dt):
    dx, dy = 0, 0

    moved = False
    if keys[pygame.K_a]:
        dx -= player.speed
        player.current_row = 3  # left
        moved = True
    elif keys[pygame.K_d]:
        dx += player.speed
        player.current_row = 2  # right
        moved = True
    elif keys[pygame.K_w]:
        dy -= player.speed
        player.current_row = 1  # up
        moved = True
    elif keys[pygame.K_s]:
        dy += player.speed
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
    collision_rects = maps[1]  

    if dx != 0:
        player_rect.x += dx
        for obstacle in collision_rects:
            try:
                if player_rect.colliderect(obstacle):
                    if dx > 0:  # Moving right
                        player_rect.right = obstacle.left
                    elif dx < 0:  # Moving left
                        player_rect.left = obstacle.right
                    break
            except TypeError as e:
                print(f"Error with collision rect: {obstacle}, error: {e}")
                continue

    if dy != 0:
        player_rect.y += dy
        for obstacle in collision_rects:
            try:
                if player_rect.colliderect(obstacle):
                    if dy > 0:  # Moving down
                        player_rect.bottom = obstacle.top
                    elif dy < 0:  # Moving up
                        player_rect.top = obstacle.bottom
                    break
            except TypeError as e:
                print(f"Error with collision rect: {obstacle}, error: {e}")
                continue

    player.x = player_rect.x
    player.y = player_rect.y

    #debug

    # Debug: Draw collision rectangles (with camera offset)
    if screen and camera:
        # Draw player rect in green (convert to screen coordinates)
        screen_player_rect = camera.apply_rect(player_rect)
        pygame.draw.rect(screen, (0, 255, 0), screen_player_rect, 2)
        
        # Draw collision rects in red (convert to screen coordinates)
        for obstacle in collision_rects:
            screen_obstacle_rect = camera.apply_rect(obstacle)

            # Only draw if visible on screen
            if screen_obstacle_rect.colliderect(pygame.Rect(0, 0, camera.screen_width, camera.screen_height)):
                pygame.draw.rect(screen, (255, 0, 0), screen_obstacle_rect, 1)


    
    