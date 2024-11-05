import math


def areodinamic_resistance (velocity: float) -> float:
    p : float = 1.23 #air densitiy
    s : float = 2.5 #car surface
    cd : float = 0.2 #aereodinamic resistance coefficient
    return 0.5 * p * math.pow(velocity,2) * s * cd

velocity = float(input("Enter velocity : "))

watt = velocity * areodinamic_resistance(velocity)
horse_power = watt/745.7

print(f"Power in watt : {watt}\nPower in horse power : {horse_power}")