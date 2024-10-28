import matplotlib.pyplot as plt
import numpy as np

def rng(n: int) -> int:
    a: int = 32310901
    b: int = 1729
    m: float = 2E24
    return (a * n  + b) % m

seed: int = 123
numbers: list[int] = []

random : int = seed

for i in range(100):
    random = rng(random)
    numbers.append(random)
    
print(numbers)