# Phase Transitions in Stochastic Moore-Connected SIR Epidemic Model
This project is a brief investigation into phase transition of viral outbreaks in context of viral persistence in a population. I used a 2D grid with Moore neighbourhood for agents and performed a parameter sweep in static infectivity condition. Further, I built a Monte Carlo simulation for uncertainty quantification. I also modified the model to account for evolution of viruses (through changes in the infectivity).
<img width="1080" height="450" alt="epidemic" src="https://github.com/user-attachments/assets/2483277f-5cb7-481d-b3ea-6c8f4b3f2afb" />
## Overview
There are two primary studies:
- **Phase Transition:** A parameter sweep of infectivity (`p`) of the virus vs mobility {`m`) of the agents on the grid. The resultant heatmap displays a critical boundary separating viral extinction from a sustained outbreak. 
- **Evolution:** To accomodate for evolution of infectivity to observe more interesting properties. The `evolve` argument is the switch between evolving and static pathogen infectivity. Further analysis will be done on this.

## Results
### Single Run for Static vs Evolving Pathogen
Each of these models were run until last infected agent recovered. Limit was capped to 200 days.
Static pathogen run with 500 agents, 70x70 grid, 45 initially infected agents, with `p = 0.1`
<img width="1080" height="450" alt="static" src="https://github.com/user-attachments/assets/8f7a0adf-39c6-41c3-b770-72c07dbe119a" />
Evolving pathogen run with 500 agents, 70x70 grid, 45 initially infected agents, with `p = 0.1` and a mutation rate of `mutrate = 0.05`
<img width="1080" height="450" alt="evolve" src="https://github.com/user-attachments/assets/07cb3fab-6175-4a32-b43b-2de81f8a9834" />
### Phase Transition (mobility vs infectivity)
Parameter scan done across a range of 30 mobility and infectivity values, with 20 iterations per value pair. I used an Intel(R) Core i7-14700HX for performing the parameter scan.
| Average Duration Heatmap | Standard Deviation (of duration) Heatmap |
| :---: | :--- |
| <img width="576" height="575" alt="avg_days_heatmap" src="https://github.com/user-attachments/assets/23818e9a-75c2-4ef4-855a-a15958e999e9" /> | <img width="576" height="575" alt="stddev_heatmap" src="https://github.com/user-attachments/assets/f190100a-f5fa-463c-b384-96f8dc0878c6" /> |

## Model Architecture


## Requirements


## How to Run


## 
