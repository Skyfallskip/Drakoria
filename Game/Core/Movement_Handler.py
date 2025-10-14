import pygame
from Core.Player_Handler import Player
from Core.Map_Loader import load_world_maps


def handle_player_movement(player, keys, dt):
    moved = False
    if keys[pygame.K_a]:
        player.x -= player.speed
        player.current_row = 3  # left
        moved = True
    elif keys[pygame.K_d]:
        player.x += player.speed
        player.current_row = 2  # right
        moved = True
    elif keys[pygame.K_w]:
        player.y -= player.speed
        player.current_row = 1  # up
        moved = True
    elif keys[pygame.K_s]:
        player.y += player.speed
        player.current_row = 0  # down
        moved = True
    if moved:
        player.animation_timer += dt
        if player.animation_timer >= player.animation_speed:

            player.current_frame = (player.current_frame + 1) % 3  # 3 frames por direção
            player.animation_timer = 0
    else:
        player.current_frame = 0  # Frame parado

def Collision_Handler(player, maps, dx, dy):
    # Get player's collision rect
    player_rect = player.get_player_rect()
    collision_rects = maps[1]  # Assuming maps[1] contains the collision rectangles

    # Handle horizontal movement collisions (dx)
    player_rect.x += dx
    for obstacle_rect in collision_rects:
        if player_rect.colliderect(obstacle_rect):
            if dx > 0:  # Moving right
                player_rect.right = obstacle_rect.left  # Stop at the left side of the obstacle
            elif dx < 0:  # Moving left
                player_rect.left = obstacle_rect.right  # Stop at the right side of the obstacle

    # Handle vertical movement collisions (dy)
    player_rect.y += dy
    for obstacle_rect in collision_rects:
        if player_rect.colliderect(obstacle_rect):
            if dy > 0:  # Moving down
                player_rect.bottom = obstacle_rect.top  # Stop at the top of the obstacle
            elif dy < 0:  # Moving up
                player_rect.top = obstacle_rect.bottom  # Stop at the bottom of the obstacle

    # After collision checks, update the player's position
    player.x = player_rect.x
    player.y = player_rect.y


    
    