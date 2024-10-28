import math


def power_formula (n: float, vs: float, ro: float, rs: float) -> float:
    return rs * math.pow(((n * vs)/(math.pow(n,2)*ro + rs)),2)

n_strat : float = 0.01
n_end : float = 2
#starting value of n
precision : float = 0.01
#used to calculate the steps
vs: int = 40
#volts amplifier
ro: int = 20
#resistance amplifier
rs: int = 8
#resistance speaker

power : list[float] = []

for n in range(1,int(n_end/precision)):
    power.append(power_formula(n*precision, vs, ro, rs))

print(max(power))