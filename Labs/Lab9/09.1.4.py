import random

def bar_code(values : list) -> None:
    max_value = max(values)
    min_value = abs(min(values)) if min(values) < 0 else 0
    asteriscs_for_unit = int(40/max(max_value,min_value))
    
    for value in values:
        if(value > 0):
            print(" "*int(asteriscs_for_unit * min_value), end="")
            print("*" * int(asteriscs_for_unit * value))
        else:
            print(" "*int(asteriscs_for_unit * (min_value - abs(value))), end="")
            print("*" * int(asteriscs_for_unit * value * - 1))

values = [random.randint(-40,40) for _ in range(10)]

print(values)

bar_code(values)