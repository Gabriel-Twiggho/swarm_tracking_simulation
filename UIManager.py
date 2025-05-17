import pygame
import Globals

class UIManager:
    def __init__(self, simulation_manager_ref):
        self.font_size = 18
        self.font = pygame.font.SysFont("Arial", self.font_size)
        self.simulation_manager = simulation_manager_ref

    #Renders text on the screen at the specified position, centre_x is True means it will centre based on x input
    def _render_text(self, text, position, color=(255, 255, 255), centre_x=False):
        text_surf = self.font.render(text, True, color)
        if centre_x:
            text_rect = text_surf.get_rect(centerx=position[0], top=position[1])
            Globals.screen.blit(text_surf, text_rect)
        else:
            Globals.screen.blit(text_surf, position)

    def _calculate_los_metrics(self):
        current_total_frames = Globals.frame_count if Globals.frame_count > 0 else 1
        
        seconds = Globals.time_target_in_los_frames / Globals.FPS
        percentage = (Globals.time_target_in_los_frames / current_total_frames) * 100
        return seconds, percentage
    
    #Draws the statistics that are displayed during the simulation runtime
    def draw_runtime_stats(self):
        elapsed_seconds = Globals.frame_count / Globals.FPS
        
        self._render_text(f"Time: {elapsed_seconds:.1f}s / {Globals.SIMULATION_DURATION_SECONDS}s", (10, 10))
        
        in_los = self.simulation_manager.is_target_in_los()
        status_text = "Target IN LOS" if in_los else "Target NOT IN LOS"
        status_color = (0, 255, 0) if in_los else (255, 100, 100)
        self._render_text(status_text, (10, 10 + self.font_size + 5), status_color)

        los_time, los_pct = self._calculate_los_metrics()
        los_frames_count = Globals.time_target_in_los_frames
        self._render_text(f"LOS Time: {los_time:.1f}s ({los_frames_count} frames)", (10, 10 + 2*(self.font_size + 5)), (0, 191, 255))
        self._render_text(f"LOS % (current): {los_pct:.1f}%", (10, 10 + 3*(self.font_size + 5)), (255, 215, 0))

    #Clears screen and displays the final simulation results.
    def display_final_results(self):
        Globals.screen.fill((0, 0, 0))

        total_simulation_frames_for_calc = Globals.SIMULATION_DURATION_SECONDS * Globals.FPS
        #fail safe check to make sure we don't divide by 0
        if total_simulation_frames_for_calc <= 0:
            total_simulation_frames_for_calc = 1 
            
        los_percentage_final = (Globals.time_target_in_los_frames / total_simulation_frames_for_calc) * 100

        text_lines = [
            f"Simulation Ended. Total Time: {Globals.SIMULATION_DURATION_SECONDS}s",
            f"Target was in Line of Sight for: {los_percentage_final:.2f}% of the time.",
            f"({Globals.time_target_in_los_frames} frames out of {int(total_simulation_frames_for_calc)} frames)",
            "Press ESCAPE to close."
        ]
        
        line_colors = [
            (255, 255, 255),
            (0, 255, 0),
            (200, 200, 200),
            (255, 255, 255)
        ]

        start_y = Globals.SCREEN_HEIGHT // 2 - (len(text_lines) * (self.font_size + 5)) // 2
        center_x_coord = Globals.SCREEN_WIDTH // 2

        for i, line_content in enumerate(text_lines):
            current_y = start_y + i * (self.font_size + 7) 
            self._render_text(line_content, (center_x_coord, current_y), line_colors[i], True)
        
        pygame.display.update()