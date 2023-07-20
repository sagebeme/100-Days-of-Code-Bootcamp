#!/usr/bin/env python3

import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up the snake
snake_pos = [(width // 2, height // 2)]
snake_size = 20
snake_color = (0, 255, 0)
snake_speed = 20

# Set up the food
food_pos = (100, 100)
food_size = 20
food_color = (255, 0, 0)

# Set up the game loop
clock = pygame.time.Clock()
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_pos[0] = (snake_pos[0][0] - snake_speed, snake_pos[0][1])
            elif event.key == pygame.K_RIGHT:
                snake_pos[0] = (snake_pos[0][0] + snake_speed, snake_pos[0][1])
            elif event.key == pygame.K_UP:
                snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - snake_speed)
            elif event.key == pygame.K_DOWN:
                snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + snake_speed)

    # Check for collision with the food
    if snake_pos[0][0] == food_pos[0] and snake_pos[0][1] == food_pos[1]:
        food_pos = (pygame.math.Vector2(snake_pos[0]) + pygame.math.Vector2((snake_size, snake_size))).xy
        snake_pos.append(snake_pos[-1])

    # Check for collision with the screen boundaries
    if snake_pos[0][0] < 0 or snake_pos[0][0] + snake_size > width or snake_pos[0][1] < 0 or snake_pos[0][1] + snake_size > height:
        running = False

    # Update the display
    screen.fill((255, 255, 255))
    for pos in snake_pos:
        pygame.draw.rect(screen, snake_color, (pos[0], pos[1], snake_size, snake_size))
    pygame.draw.rect(screen, food_color, (food_pos[0], food_pos[1], food_size, food_size))
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(10)

# Clean up the game resources
pygame.quit()
