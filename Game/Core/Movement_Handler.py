import pygame

def handle_player_movement(player, keys, dt):
    moved = False
    if keys[pygame.K_a]:
        player.x -= player.speed
        player.current_row = 7  # left
        moved = True
    elif keys[pygame.K_d]:
        player.x += player.speed
        player.current_row = 3  # right
        moved = True
    elif keys[pygame.K_w]:
        player.y -= player.speed
        player.current_row = 5  # up
        moved = True
    elif keys[pygame.K_s]:
        player.y += player.speed
        player.current_row = 1  # down
        moved = True
    if moved:
        player.animation_timer += dt
        if player.animation_timer >= player.animation_speed:
            player.current_frame = (player.current_frame + 1) % 5  # 3 frames per direction
            player.animation_timer = 0
    else:
        player.current_frame = 0  # Idle frame