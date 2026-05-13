## age sus is age susceptibility
import numpy as np

class Agent:
    def __init__(self, agent_id, x, y, age_group=None):
        self.agent_id = agent_id
        self.x = x
        self.y = y
        
        if age_group is None:
            self.age_group = np.random.choice(['y','a','o'], p=[0.3,0.5,0.2])
        else:
            self.age_group = age_group
            
        age_sus = {
            'y': 0.03,
            'a':0.05,
            'o': 0.10
            }
        
        base = age_sus[self.age_group]
        self.inf_prob = np.clip(base + np.random.normal(0,0.01), 0.01, 0.20)
        self.state = 's'
        self.inf_day = 0
        self.recover = max(5, int(np.random.normal(10,2)))
        
    def moving(self, grid, mobility = 1):
        if mobility <= 1:
            size = 1
        else:
            size = np.random.randint(1, mobility+1)
        dx = np.random.choice([-1,0,1])*size
        dy = np.random.choice([-1, 0, 1])*size
        self.x = np.clip(self.x + dx, 0, grid-1)
        self.y = np.clip(self.y + dy, 0, grid-1)
        
    def infect(self, over = None, mutrate = 0.01):
        if self.state == 's':
            if over is not None:
                prob = over
            else:
                prob = self.inf_prob
            if np.random.random() < prob:
                self.state = 'i'
                self.inf_prob = np.clip(prob+np.random.normal(0,mutrate), 0.005, 0.99)
                return True
        else:
            return False
    def update(self):
        if self.state == 'i':
            self.inf_day += 1
            if self.inf_day >= self.recover:
                self.state = 'r'
                
    def __repr__(self):
        return (f"Agent(id={self.agent_id}, state={self.state}, age={self.age_group}, pos=({self.x},{self.y}))")
                