import pygame
from typing import List
from GameObject import GameObject
import Globals
#from Agent import Agent

'''
properties and behavior of an individual station, including how it's drawn.

'''

class Station(GameObject):
    def __init__(self, x: float, y: float, name: str = "Station"):
        super().__init__(x, y)
        self.name = name

    #@property
    #def numAgentsDeployedHere(self):
    #    return+ len(self.agentsDeployedHere)
    
    def Update(self):
        #This is only done as Gameobject class is inherited and recquires update function.
        pass

    def Draw(self):
        #draw station
        pygame.draw.rect(Globals.screen, (0, 0, 255), (self.x - 5, self.y - 5, 10, 10))

        #draw station name
        font = pygame.font.Font(None, 24)
        text = font.render(self.name, True, (200,200,200))
        Globals.screen.blit(text, (self.x - 50, self.y + 10))