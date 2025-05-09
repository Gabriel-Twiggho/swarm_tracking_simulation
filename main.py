'''import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1750, 950
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Script")

# Define colors
WHITE = (0, 0, 0)
BLUE = (255, 0, 255)

# Circle properties
x, y = width // 2, height // 2
radius = 30
speed_x, speed_y = 3, 3

# Main loop
running = True
while running:
    pygame.time.delay(30)  # Control frame rate
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update circle position
    x += speed_x
    y += speed_y

    # Bounce off walls
    if x - radius < 0 or x + radius > width:
        speed_x *= -1
    if y - radius < 0 or y + radius > height:
        speed_y *= -1

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (x, y), radius)
    pygame.display.update()

# Quit Pygame
pygame.quit()'''

import pygame
from GameObject import GameObject
from Target import Target

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1750, 950
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Script")

# Define colors
BLACK = (0, 0, 0)  # White background

# Create Target object
_target = Target(1000, 500)

# Set up clock for frame rate control
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update target
    _target.input_handler()  # Handle arrow key input
    _target.update()         # Move target based on dx, dy

    # Draw
    screen.fill(BLACK)       # Clear screen with white background
    _target.draw(screen)     # Draw target

    pygame.display.update()
    clock.tick(60)

# Quit Pygame
pygame.quit()