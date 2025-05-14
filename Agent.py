import pygame
import Globals
from GameObject import GameObject
from Target import Target

from typing import List, Tuple
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from AgentManager import AgentManager
import math
import numpy as np


#implement repulsive strength proporsional to distance.
#make boundaries for swarm and target
#scale down LOS of swarm
#implement goal tracking
#implement standard time for simulation

class Agent(GameObject):
    tmem=300
    speed=5
    communicationAmount=5

    def __init__(self, x: float, y: float, manager: 'AgentManager'):
        super().__init__(x, y)
        self._manager=manager
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self._losRange=50
        self.lsx=None   #last sighting x position
        self.lsy=None   #last sighting y postion
        self.lst=None   #last sighting time
        self.repulsiveForce:float=10000.0
        self.repulsiveForceMin=10000.0
        self.repulsiveForceMax=100000.0
        #self.inertia_weight = 0.01

    def _enforce_bounds(self):
        #clamp x positio
        if self.x < Globals.TOPLEFT_X:
            self.x = Globals.TOPLEFT_X
        elif self.x > Globals.BOTTOMRIGHT_X:
            self.x = Globals.BOTTOMRIGHT_X
        
        #clamp y position
        if self.y < Globals.TOPLEFT_Y:
            self.y = Globals.TOPLEFT_Y
        elif self.y > Globals.BOTTOMRIGHT_Y:
            self.y = Globals.BOTTOMRIGHT_Y

    def Update(self):
        self.Algo()
        self.x += self.velocity_x
        self.y += self.velocity_y
        self._enforce_bounds()
        self.CanSeeTarget() 


    def Draw(self):
        if self.CanSeeTarget():
            color = (255, 255, 0)
        else:
            color=(255, 255, 255)
        pygame.draw.circle(Globals.screen, color, (int(self.x), int(self.y)), 4)
        pygame.draw.circle(Globals.screen, color, (int(self.x), int(self.y)), self._losRange,1)

    def CanSeeTarget(self) -> bool:
        target=Target.get_instance()
        if(self._losRange**2>(self.x-target.x)**2+(self.y-target.y)**2):
            self.lsx=target.x
            self.lsy=target.y
            self.lst=Globals.frame_count
            return True
        else:
            return False
        
    def _get_k_nearest_neighbours(self) -> List['Agent']:
        all_other_agents = [agent for agent in self._manager._agents if agent is not self]

        distances: List[Tuple[float, Agent]] = []
        for _agent in all_other_agents:
            dist = self.Distance(self.x, self.y, _agent.x, _agent.y)
            distances.append((dist, _agent))

        distances.sort(key=lambda item: item[0])
        k_nearest = []
        for i in range(self.communicationAmount):
            dist, agent = distances[i]
            k_nearest.append(agent)

        return k_nearest

    
    def Algo(self):
        va = np.array([0.0, 0.0])
        vr = np.array([0.0, 0.0])
        #vi = np.array([0.0, 0.0])

        neighbours = self._get_k_nearest_neighbours()
        best_sighting_x = None
        best_sighting_y = None
        best_sighting_time = -1
        
        if self.lst is not None and (Globals.frame_count - self.lst) < self.tmem:
            best_sighting_x = self.lsx
            best_sighting_y = self.lsy
            best_sighting_time = self.lst

        #check k nearest neighbours
        for neighbour in neighbours:
            if neighbour.lst is not None and (Globals.frame_count - neighbour.lst) < self.tmem:
                if neighbour.lst > best_sighting_time:
                    best_sighting_x = neighbour.lsx
                    best_sighting_y = neighbour.lsy
                    best_sighting_time = neighbour.lst
        
        '''
        #finding best agent 
        self.bestagent: Agent = None

        for _agent in self._manager._agents:        
            if (_agent.lst is not None and _agent.lst>Globals.frame_count-self.tmem): #if lst
                if self.bestagent is None:
                    self.bestagent = _agent
                elif self.bestagent is not None and _agent.lst > self.bestagent.lst:
                    self.bestagent = _agent
        
        #calculating Va
        if self.bestagent is not None:
            va = np.array([self.bestagent.lsx, self.bestagent.lsy]) - np.array([self.x, self.y])
            va = self.Normalize(va)
        '''
        #calculating Va
        if best_sighting_x is not None:
            va = np.array([best_sighting_x, best_sighting_y]) - np.array([self.x, self.y])
            va = self.Normalize(va)

        #adaptive vr
        if self.CanSeeTarget():
            if self.repulsiveForce > self.repulsiveForceMin:
                self.repulsiveForce-=1000
        else:
            if self.repulsiveForce < self.repulsiveForceMax:
                self.repulsiveForce+=0.1

        #calculating vr
        for _agent in self._manager._agents:
            if _agent is self: #dont repel self
                continue

            idv_vr = np.array([0.0, 0.0])
            idv_vr = np.array([self.x, self.y]) - np.array([_agent.x, _agent.y])
            idv_vr = self.Normalize(idv_vr)
            idv_vr=idv_vr/((self.Distance(self.x,self.y,_agent.x,_agent.y)+1))**2
            
            vr += idv_vr
        #vr = self.Normalize(vr)
        vr=vr/len(self._manager._agents)

        #calculating inertia velocit (vi)
        #vi = self.Normalize(np.array([self.velocity_x, self.velocity_y]))
        #v_new = self.Normalize(va+vr*self.repulsiveForce + vi*self.inertia_weight)

        v_new = self.Normalize(va+vr*self.repulsiveForce)
        self.velocity_x = v_new[0]
        self.velocity_y = v_new[1]





    @staticmethod
    def Distance(x1, y1, x2, y2):
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    @staticmethod
    def Normalize(vector):
        magnitude=np.linalg.norm(vector)
        return vector / magnitude if magnitude != 0 else vector
            

    

