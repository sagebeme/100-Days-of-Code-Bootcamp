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

# Set up the food
food_pos = (100, 100)
food_size = 20
food_color = (255, 0, 0)
