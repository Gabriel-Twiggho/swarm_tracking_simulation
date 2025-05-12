import pygame
from typing import List
from GameObject import GameObject
#from Agent import Agent

'''
properties and behavior of an individual station, including how it's drawn.

'''

class Station(GameObject):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)
        self.agentsDeployedHere: List[Agent] = []

    #@property
    #def numAgentsDeployedHere(self):
    #    return len(self.agentsDeployedHere)
    
    def Update(self):
        #This is only done as Gameobject class is inherited and recquires update function.
        pass

    def Draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x - 5, self.y - 5, 10, 10))