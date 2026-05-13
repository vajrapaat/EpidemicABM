import numpy as np
import pandas as pd
from model import Model

def monte_carlo(runs = 200, agent= 500, grid = 50, day=200, inf_range = (3,10), evolve=False, mobility=1, p = None):
    results = []
    all_curves = []
    print(f"Starting Monte Carlo Sim: {runs} runs")
    
    for run_id in range(runs):
       # if run_id % 50 == 0:
        print(f" Run {run_id}/{runs}")
        
        init_infect = np.random.randint(*inf_range)
        model = Model(n=agent, grid=grid, init_infect=init_infect,seed=run_id, p=p)
        history = model.run(day=day)
        infected_series = np.array(history['i'])
        
        results.append({
            'run_id':             run_id,
            'peak_infected':      infected_series.max(),
            'peak_infected_pct':  infected_series.max() / agent * 100,
            'peak_day':           infected_series.argmax(),
            'total_recovered':    history['r'][-1],
            'attack_rate_pct':    history['r'][-1] / agent * 100,
            'epidemic_ended':     history['i'][-1] == 0
        })
        
        padded = np.pad(infected_series,(0,day + 1 - len(infected_series)), constant_values=0)
        all_curves.append(padded)
        
    df = pd.DataFrame(results)
    curves = np.array(all_curves)
    print("Completed!!")
    print(df[['peak_infected_pct','attack_rate_pct','peak_day']].describe().round(2))
    return df, curves



