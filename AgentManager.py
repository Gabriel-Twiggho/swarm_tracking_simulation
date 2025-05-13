from typing import List
from Agent import Agent

class AgentManager:
    def __init__(self):
        self._agents: List[Agent] = []
        self._numOfAgents=12
        self.deploy_agents()

    def deploy_agents(self):
        for i in range(self._numOfAgents):
            x = (450 * (i % 4)) + 200
            y = 150 + 300 * (i // 4)
            new_agent = Agent(x, y,self)
            self._agents.append(new_agent)


    
    def update_agents(self):
        for agent in self._agents:
            agent.Update()
        

    def DrawAgents(self):
        for agent in self._agents:
            agent.Draw()


    def CanSeeTarget(self):
        for agent in self._agents:
            if agent.CanSeeTarget(): return True
        else: return False



        