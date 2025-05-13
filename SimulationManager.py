import pygame
from typing import List
from AgentManager import AgentManager
from Target import Target
from Agent import Agent
from StationManager import StationManager

class SimulationManager:
    def __init__(self):
        self._target = Target.get_instance(1000, 500)
        self._agentManager=AgentManager()
        self._stationManager = StationManager()
        

    def Update(self):
        self._target.Update()
        self._agentManager.update_agents()
        self._stationManager.Update()

    def Draw(self):
        self._target.Draw()
        self._agentManager.DrawAgents()
        self._stationManager.Draw()