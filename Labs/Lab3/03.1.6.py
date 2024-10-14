x: int = int(input("Number x : "))

disequation_1: bool = x <= 0 or x >= 100
disequation_2: bool = x <= 0 and x >= 100
disequation_3: bool = x <= 0 and 100 >= x
disequation_4: bool = x <= 0 or x >= 100 and x != -1

print(f"not({x} > 0 and {x} < 100)", disequation_1)
print(f"not({x} > 0 or {x} < 100)", disequation_2)
print(f"not({x} > 0 or 100 < {x})", disequation_3)
print(f"not({x} > 0 and{x} < 100 or {x} == -1)", disequation_4)