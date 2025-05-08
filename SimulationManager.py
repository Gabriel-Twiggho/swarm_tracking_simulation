import pygame
from typing import List
from Agent import Agent
from Station import Station
from Target import Target

class SimulationManager:
    def __init__(self):
        self.agents: List[Agent] = []
        self.stations: List[Station] = []
        self.targets: List[Target] = []

    def update(self):
        for agent in self.agents:
            agent.update()

    def draw(self, screen):
        for station in self.stations:
            station.draw(screen)
        for agent in self.agents:
            agent.draw(screen)
        for target in self.targets:
            target.draw(screen)