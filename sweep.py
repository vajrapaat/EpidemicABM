import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from model import Model
from joblib import Parallel, delayed

def run_one(m,p):
    model = Model(n=2000, grid=150, p = p, evolve=False)
    history = model.run(day=500, mobility=m)
    return {
        'max_mobility': m,
        'inf_prob': p,
        'duration': len(history['day']),
        'peak': max(history['i'])}
    
    
def paramsweep(iter):
    inf_probs = np.linspace(0.01,0.45,30)
    maxmob = np.linspace(1,30,30)
    tasks = [(m, p) for m in maxmob for p in inf_probs for _ in range(iter)]
    print(f"Distribution = {len(tasks)}")
    raw_results = Parallel(n_jobs=-1, verbose=10)(delayed(run_one)(m, p) for m, p in tasks)
    df_raw = pd.DataFrame(raw_results)
    summary = df_raw.groupby(['max_mobility', 'inf_prob']).agg(avg_duration=('duration', 'mean'),std_duration=('duration', 'std'),avg_peak=('peak', 'mean')).reset_index()
    summary['avg_peak_pct'] = (summary['avg_peak'] / 2000) * 100
    return summary
if __name__ == "__main__":
    df = paramsweep(iter=20)
    df.to_csv("simdata.csv", index=False) 
    fintable = df.pivot(index='max_mobility', columns='inf_prob', values='avg_duration')
    sns.heatmap(fintable, cmap='magma', annot=False)
    plt.ylabel("Max Step Size (mobility)")
    plt.xlabel("Infectivity")
    plt.savefig('ridge.png')
    plt.show()
