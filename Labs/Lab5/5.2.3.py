prey : float = 1000
predators : float = 20
A: float = 0.1
B: float = 0.01
C: float = 0.01
D: float = 0.00002


simulation_steps: int = 100


for i in range(simulation_steps):
    #update preys and predators
    prey_temp: float = prey * (1+A-B*predators)
    predators_temp: float = predators * (1-C+D*prey)
    #save new prey and predators
    prey = prey_temp
    predators = predators_temp
    print(f"Preys : {prey}, Predators : {predators}")