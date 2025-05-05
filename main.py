import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Script")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

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
pygame.quit()