import pygame
from SimulationManager import SimulationManager
from UIManager import UIManager
import Globals

# Initialize Pygame
pygame.init()
pygame.font.init()

_simulationManager=SimulationManager()
_uiManager = UIManager(_simulationManager)
clock = pygame.time.Clock()


while Globals.simulation_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Globals.simulation_running = False

    #update sim logic
    if Globals.frame_count < Globals.SIMULATION_DURATION_SECONDS * Globals.FPS:
        Globals.frame_count += 1
        _simulationManager.Update()
        if _simulationManager.is_target_in_los():
            Globals.time_target_in_los_frames += 1
    else:
        Globals.simulation_running = False

    # Draw
    Globals.screen.fill((0, 0, 0))
    _simulationManager.Draw()
    _uiManager.draw_runtime_stats()

    pygame.display.update()
    clock.tick(Globals.FPS)

#after sim ends
_uiManager.display_final_results()

#keep window open after sim ends until user closes it
post_simulation_running = True
while post_simulation_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            post_simulation_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Allow closing with ESC
                post_simulation_running = False

pygame.quit()