import math

Q1: float  = float(input("Q1 : "))
Q2: float  = float(input("Q2 : "))
R: float  = float(input("R : "))

𝜀: float = 8.854E-12 

force = (Q1 * Q2) / (4 * math.pi * pow(R, 2) * 𝜀)

print(force)