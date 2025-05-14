import pygame
from Target import Target
from SimulationManager import SimulationManager
import Globals

# Initialize Pygame
pygame.init()
pygame.font.init()
ui_font = pygame.font.SysFont("Arial", 15)


_simulationManager=SimulationManager()
clock = pygame.time.Clock()

#helper functions
def render_text(surface, text, position, color=(255, 255, 255)):
    text_surf = ui_font.render(text, True, color)
    surface.blit(text_surf, position)

def update_simulation():
    if Globals.frame_count < Globals.SIMULATION_DURATION_SECONDS * Globals.FPS:
        Globals.frame_count += 1
        _simulationManager.Update()
        if _simulationManager.is_target_in_los():
            Globals.time_target_in_los_frames += 1
    else:
        Globals.simulation_running = False

def calculate_los_metrics():
    seconds = Globals.time_target_in_los_frames / Globals.FPS
    percentage = (Globals.time_target_in_los_frames / Globals.frame_count * 100) if Globals.frame_count > 0 else 0.0
    return seconds, percentage

#draw elpased time, LOS metrics
def draw_stats():
    elapsed = Globals.frame_count / Globals.FPS
    frames = Globals.time_target_in_los_frames
    render_text(Globals.screen, f"Time: {elapsed:.1f}s / {Globals.SIMULATION_DURATION_SECONDS}s", (10, 10))
    
    #is LOS
    in_los = _simulationManager.is_target_in_los()
    status_text = "Target in LOS" if in_los else "Target out of LOS"
    status_color = (0, 255, 0) if in_los else (255, 0, 0)
    render_text(Globals.screen, status_text, (10, 40), status_color)

    #LOS %, seconds
    los_time, los_pct = calculate_los_metrics()
    render_text(Globals.screen, f"LOS Time: {los_time:.1f}s ({frames} frames)", (10, 70), (0, 191, 255))
    render_text(Globals.screen, f"LOS %: {los_pct:.1f}%", (10, 100), (255, 215, 0))

#screen after sim ends
def display_final_results():
    total_frames = Globals.SIMULATION_DURATION_SECONDS * Globals.FPS
    percent_final = (Globals.time_target_in_los_frames / total_frames * 100) if total_frames > 0 else 0.0
    line1 = f"Target was in Line of Sight for: {percent_final:.2f}% of the time."
    line2 = f"({Globals.time_target_in_los_frames} frames out of {int(total_frames)} frames)"
    Globals.screen.fill((0, 0, 0))
    render_text(Globals.screen, line1, (10, 10))
    render_text(Globals.screen, line2, (10, 40))
    pygame.display.update()


while Globals.simulation_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Globals.simulation_running = False

    update_simulation()

    # Draw
    Globals.screen.fill((0, 0, 0))
    _simulationManager.Draw()
    draw_stats()

    pygame.display.update()
    clock.tick(Globals.FPS)

#after sim ends
display_final_results()

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