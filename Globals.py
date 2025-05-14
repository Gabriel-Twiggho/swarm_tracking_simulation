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