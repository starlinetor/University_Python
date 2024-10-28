import matplotlib.pyplot as plt

prey: float = 1000
predators: float = 20

prey_graph: list[float] = [prey]
predators_graph: list[float] = [predators]

A: float = 0.1
B: float = 0.01
C: float = 0.01
D: float = 0.00002


simulation_steps: int = 1000
simulation_graph: list[float] = [0]


for i in range(1,simulation_steps):
    #update preys and predators
    prey_temp: float = prey * (1+A-B*predators)
    predators_temp: float = predators * (1-C+D*prey)
    #save new prey and predators
    prey = prey_temp
    predators = predators_temp
    #save data for graph
    simulation_graph.append(i)
    prey_graph.append(prey)
    predators_graph.append(predators)
    
#render graph
plt.plot(simulation_graph, prey_graph, label = "Prey")
plt.plot(simulation_graph, predators_graph, label = "Predators")

plt.xlabel("Simulation Steps")
plt.ylabel("Number of induals")

plt.legend()
plt.show()