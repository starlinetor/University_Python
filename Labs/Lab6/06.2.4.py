import math
from re import A

resistivity_table : dict[str:float] = {
    "aluminum" : 2.82E-8,
    "copper" : 1.678E-8
}


def diameter(wire_gauge : int) -> float:
    return 0.127 * math.pow(92, (36-wire_gauge)/39)

def wire_resistance(material: str, lenght: float, wire_gauge) -> float:
    resistivity = resistivity_table.get(material)
    return (4 * resistivity * lenght) / (math.pi * math.pow(diameter(wire_gauge),2))

print(wire_resistance("copper", 10, 1))
print(wire_resistance("aluminum", 10, 1))