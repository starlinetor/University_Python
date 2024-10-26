import math

T : float = 6
𝜆 : float = math.log(2) / 6
A0 : float = 1

for t in range(24):
    A: float = A0 * pow(math.e, -𝜆* t)
    print(f"{round( A / A0 * 100, 2)}%")