import pygame
SCREEN_WIDTH = 1750
SCREEN_HEIGHT = 950
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Swarm Simulation")
frame_count=0

#Boundary limits
TOPLEFT_X = 0
TOPLEFT_Y = 0
BOTTOMRIGHT_X = SCREEN_WIDTH
BOTTOMRIGHT_Y = SCREEN_HEIGHT

SIMULATION_DURATION_SECONDS = 14
FPS = 60

time_target_in_los_frames = 0
simulation_running = True

#Target control settings
TARGET_CONTROL_MODE = "AUTO"  # Options: "MANUAL", "AUTO"

# Define path parameters if AUTO mode is selected
TARGET_AUTO_PATH_RECT = {
    "x": 0,          # Top-left X of the rectangle
    "y": 475,          # Top-left Y of the rectangle
    "width": 1750,     # Width of the rectangle
    "height": 40,     # Height of the rectangle
    "initial_x": 1500, # Default initial X (used if manual or if auto path doesn't set it)
    "initial_y": 500   # Default initial Y
}