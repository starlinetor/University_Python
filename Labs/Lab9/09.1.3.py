import random


def bar_code(values : list) -> None:
    max_value = max(values)
    asteriscs_for_unit = int(40/max_value)
    
    for value in values:
        print("*" * int(asteriscs_for_unit * value))

values = [random.randint(1,40) for _ in range(10)]

print(values)

bar_code(values)