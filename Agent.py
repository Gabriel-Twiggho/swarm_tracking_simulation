import pygame
from GameObject import GameObject

class Agent(GameObject):
    def __init__(self, x: float, y: float, velocity_x: float, velocity_y: float):
        super().__init__(x, y)
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.seeTarget = False
        self._losRange=50

    def Update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y


    def Draw(self, screen):
        color = (0, 255, 0) if self.seeTarget else (255, 255, 0)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), 5)

