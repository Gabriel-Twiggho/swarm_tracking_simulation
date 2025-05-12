import pygame
from typing import List
from GameObject import GameObject
from Agent import Agent

class Station(GameObject):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)
        self.agentsDeployedHere: List[Agent] = []

    @property
    def numAgentsDeployedHere(self):
        return len(self.agentsDeployedHere)

    def Draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x - 5, self.y - 5, 10, 10))