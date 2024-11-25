import random

def bar_code(values : list, captions : list) -> None:
    max_value = max(values)
    asteriscs_for_unit = int(40/max_value)
    
    for i in range(len(values)):
        print(captions[i],"*" * int(asteriscs_for_unit * values[i]))

values = [random.randint(1,40) for _ in range(10)]
captions = [f"string_{i}" for i in range(10)]

print(values)

bar_code(values, captions)