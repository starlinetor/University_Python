import random
from xmlrpc.client import Boolean

def switch_first_last(values : list) -> list: 
    values = values.copy()
    values[0], values[len(values)-1] = values[len(values)-1], values[0]
    return values

def shift_right(values : list) -> list:
    values = values.copy()
    last_value = values[len(values)-1]
    for i in range(len(values)-1,0,-1):
        values[i] = values[i-1]
    values[0] = last_value
    return values

def even_to_zero(values: list [int]) -> list[int]:
    values = values.copy()
    for value in values:
        if value % 2 == 0:
            values[values.index(value)] = 0
    return values

def major_element(values : list) -> list:
    values_new = values.copy()
    for i in range(1, len(values)-1):
        values_new[i] = max(values[i-1], values[i+1])
    return values_new

def remove_center(values : list) -> list:
    values = values.copy()
    lenght = len(values)
    if(lenght %2 == 0):
        values.pop(int(lenght/2-1))
        values.pop(int(lenght/2-1))
    else:
        values.pop(int(lenght-1/2))
    return values

def even_to_the_end(values: list[int]) -> list[int]:
    values_new = values.copy()
    moved_values = 0
    for i in range(len(values)):
        if values[i] %2 == 0:
            values_new.append(values_new.pop(i-moved_values))
            moved_values += 1
    return values_new

def second_max(values : list) -> list:
    values = values.copy()
    values.remove(max(values))
    return max(values)

def is_sorted(values : list) -> bool:
    values_new = sorted(values.copy())
    if values_new == values:
        return True
    else:
        return False

def close_duplicates(values: list) -> bool:
    for i in range(len(values)-1):
        if values[i] == values[i+1]:
            return True
    return False

def duplicates(values: list) -> bool:
    values = sorted(values.copy())
    return close_duplicates(values)

values = [random.randint(0,9) for _ in range(5)]

print(values)

print(switch_first_last(values))

print(shift_right(values))

print(even_to_zero(values))

print(major_element(values))

print(remove_center(values))

print(even_to_the_end(values))

print(second_max(values))

print(is_sorted(values))

print(close_duplicates(values))

print(duplicates(values))