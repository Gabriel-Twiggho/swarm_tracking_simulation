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

SIMULATION_DURATION_SECONDS = 10
FPS = 60

time_target_in_los_frames = 0
simulation_running = True