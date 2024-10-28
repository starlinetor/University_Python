import math
import matplotlib.pyplot as plt

def power_formula (n: float, vs: float, ro: float, rs: float) -> float:
    return rs * math.pow(((n * vs)/(math.pow(n,2)*ro + rs)),2)

n_strat : float = 0.01
n_end : float = 2
#starting / ending value of n
precision : float = 0.01
#used to calculate the steps
vs: int = 40
#volts amplifier
ro: int = 20
#resistance amplifier
rs: int = 8
#resistance speaker

power : list[float] = []
n_graph : list[float] = []

for n in range(1,int(n_end/precision)):
    power.append(power_formula(n*precision, vs, ro, rs))
    n_graph.append(n*precision)

max_power: float = max(power)
optimal_ratio: float = power.index(max_power) * precision

print(f"Max power of {max_power} found with a ratio of 1 : {optimal_ratio}")

plt.plot(n_graph, power, label = "Power to coil ratio")
plt.plot((optimal_ratio,optimal_ratio), (0, max_power), label = "Max power")

plt.xlabel("Coil ratio")
plt.ylabel("Power")

plt.legend()
plt.show()