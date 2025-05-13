import pygame
import Globals
from GameObject import GameObject
from Target import Target

from typing import List
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from AgentManager import AgentManager
import math
import numpy as np


class Agent(GameObject):
    tmem=300
    speed=5
    communicationAmount=5
    def __init__(self, x: float, y: float, manager: 'AgentManager'):
        super().__init__(x, y)
        self._manager=manager
        self.velocity_x = 0
        self.velocity_y = 0
        self._losRange=100
        self.lsx=None#last sighting x position
        self.lsy=None#last sighting y postion
        self.lst=None#last sighting time
        self.repulsiveForce:float=6
        self.repulsiveForceMin=2
        self.repulsiveForceMax=12

    def Update(self):
        self.Algo()
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.CanSeeTarget()


    def Draw(self):
        if self.CanSeeTarget():
            color = (255, 255, 0)
        else:
            color=(255, 255, 255)
        pygame.draw.circle(Globals.screen, color, (int(self.x), int(self.y)), 4)
        pygame.draw.circle(Globals.screen, color, (int(self.x), int(self.y)), self._losRange,1)

    def CanSeeTarget(self):
        target=Target.get_instance()
        if(self._losRange**2>(self.x-target.x)**2+(self.y-target.y)**2):
            self.lsx=target.x
            self.lsy=target.y
            self.lst=Globals.frame_count
            return True
        else:
            return False
    

    
    def Algo(self):
        va = np.array([0.0, 0.0])
        vr = np.array([0.0, 0.0])
        vi = np.array([0.0, 0.0])

        self.bestagent: Agent = None
        for _agent in self._manager._agents:        
            if (_agent.lst is not None and _agent.lst>Globals.frame_count-self.tmem):
                if self.bestagent is None:
                    self.bestagent = _agent
                elif self.bestagent is not None and _agent.lst > self.bestagent.lst:
                    self.bestagent = _agent

        if self.bestagent is not None:
            va = np.array([self.bestagent.lsx, self.bestagent.lsy]) - np.array([self.x, self.y])
            va = self.Normalize(va)



        if self.CanSeeTarget==True: #and self.repulsiveForce>self.repulsiveForceMin:
            self.repulsiveForce-=0.1
        elif self.CanSeeTarget==False: #and self.repulsiveForce<self.repulsiveForceMax:
            self.repulsiveForce+=0.01

        if self.CanSeeTarget() == False:
            for _agent in self._manager._agents:
                idv_vr = np.array([0.0, 0.0])
                idv_vr = np.array([self.x, self.y]) - np.array([_agent.x, _agent.y])
                idv_vr = self.Normalize(idv_vr)
                vr += idv_vr
            vr = self.Normalize(vr)

        vi = self.Normalize(np.array([self.velocity_x, self.velocity_y]))

        v_new = self.Normalize(va+self.repulsiveForce*vr*0.01)
        self.velocity_x = v_new[0]
        self.velocity_y = v_new[1]

            
    




                

    
    @staticmethod
    def Distance(self, agent2 ):
        return math.sqrt((self.x-agent2.x)**2+(self.y-agent2.y)**2)
    
    @staticmethod
    def Normalize(vector):
        magnitude=np.linalg.norm(vector)
        return vector / magnitude if magnitude != 0 else vector
            

    

