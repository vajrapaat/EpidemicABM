import numpy as np
from agent import Agent

class Model:
    def __init__(self, n=500, grid=50, init_infect = 5, seed=None, p=None, mutrate = 0.01, evolve = True):
        if seed is not None:
            np.random.seed(seed)
        self.mutrate = mutrate
        self.evolve = evolve
        self.grid = grid
        self.n = n
        self.day = 0
        self.agents = []
        for i in range(n):
            x = np.random.randint(0, grid)
            y = np.random.randint(0, grid)
            self.agents.append(Agent(i,x,y))
            
        init_infect = np.random.choice(self.agents, init_infect, replace=False)
        for agent in init_infect:
            agent.state = 'i'
            if p is not None:
                agent.inf_prob = p
        self.history = {'s':[], 'i':[], 'r':[], 'day':[], 'snapshot':[], 'mean_inf':[]}
        self._record()
        
        
        
    def _record(self):
        states = [a.state for a in self.agents]
        self.history['day'].append(self.day)
        self.history['s'].append(states.count('s'))
        self.history['i'].append(states.count('i'))
        self.history['r'].append(states.count('r'))
        snaps = {'s':[], 'i': [], 'r':[]}
        for agents in self.agents:
            snaps[agents.state].append((agents.x,agents.y))
        self.history['snapshot'].append(snaps)
        infected = [a for a in self.agents if a.state == 'i']
        if infected:
            self.history['mean_inf'].append(np.mean([a.inf_prob for a in infected]))
        else:
            last = self.history['mean_inf'][-1] if self.history['mean_inf'] else 0
            self.history['mean_inf'].append(last)
            
    def _get_neighbors(self, agent, radius = 1):
        neighbors = []
        for other in self.agents:
           if other.agent_id == agent.agent_id:
               continue
           dist = max(abs(other.x - agent.x), abs(other.y - agent.y))
           if dist <= radius:
               neighbors.append(other)
        return neighbors
    def step(self, mobility = 1):
        self.day += 1
        for agent in self.agents:
            agent.moving(self.grid, mobility)
            
        inf_agent = [a for a in self.agents if a.state == 'i']
        for infected in inf_agent:
            for neighbor in self._get_neighbors(infected):
                if neighbor.state == 's':
                    neighbor.infect(over = infected.inf_prob, mutrate=self.mutrate if self.evolve else 0.0)
                    
        for agent in self.agents:
            agent.update()
        self._record()
        
    def run(self, day = 200, mobility = 1):
        for _ in range(day):
            self.step(mobility=mobility)
            if self.history['i'][-1] == 0:
                break
        return self.history
    