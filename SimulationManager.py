import pygame
from typing import List
from AgentManager import AgentManager
from Target import Target

class SimulationManager:
    def __init__(self):
        self._agentManager = AgentManager()
        self._target = Target(1000, 500)

    def Update(self):
        self._target.input_handler()
        self._target.Update()

    def Draw(self):
        self._target.Draw()
