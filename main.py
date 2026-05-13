from model import Model
from montecarlo import monte_carlo
from plots import (plot_single_run, plot_mc_uncert, plot_outcome_dist, plot_evolution, animate_epidemic)
import matplotlib.pyplot as plt

if __name__ == "__main__":

    print("Single run static")
    model_static = Model(n=500, grid=70, init_infect=45, seed=42, p=0.1, evolve=False)
    history_static = model_static.run(day=200, mobility=4)
    plot_single_run(history_static)
    plt.title("Single Run Static")
    plt.show()
    animate_epidemic(history_static, model_static.agents, grid_size=70, filename='static.gif')

    print("Single run evolving")
    model_evolve = Model(n=500, grid=70, init_infect=45, seed=42, p=0.1, evolve=True, mutrate=0.05)
    history_evolve = model_evolve.run(day=200, mobility=4)
    plot_single_run(history_evolve)
    plt.title("Single Run Evolving")
    plt.show()
    plot_evolution(history_evolve)
    animate_epidemic(history_evolve, model_evolve.agents, grid_size=70, filename='evolve.gif')
    

    print("Monte Carlo normal")
    df_normal, curves_normal = monte_carlo(runs=50, agent=500, grid=70, day=200, evolve=False, mobility=6, p=0.1010)
    plot_mc_uncert(curves_normal, 500)
    plot_outcome_dist(df_normal)


    print("Monte Carlo ridge")
    df_ridge, curves_ridge = monte_carlo(runs=50, agent=500, grid=70, day=200, evolve=False, mobility=6, p=0.2527)
    plot_mc_uncert(curves_ridge, 500) 
    plot_outcome_dist(df_ridge)

    print("Done!!")