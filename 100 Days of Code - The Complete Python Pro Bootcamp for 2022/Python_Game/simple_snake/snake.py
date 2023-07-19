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

# Set up the game loop
clock = pygame.time.Clock()
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game objects
    # TODO: Implement snake movement and collision detection

    # Draw the game objects
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, snake_color, (snake_pos[0][0], snake_pos[0][1], snake_size, snake_size))
    pygame.draw.rect(screen, food_color, (food_pos[0], food_pos[1], food_size, food_size))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(10)

# Clean up the game resources
pygame.quit()
