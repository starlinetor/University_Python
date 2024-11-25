def remove_min_max(values : list[int]) -> list[int]:
    values = values.copy()
    values.remove((max(values)))
    values.remove(min(values))
    return values

def remove_even(values : list[int]) -> list[int]:
    values_new = values.copy()
    for value in values:
        if value%2!=0:
            values_new.remove(value)
    return values_new

def remove_not_2_digit(values : list[int]) -> list[int]:
    values_new = values.copy()
    for value in values:
        if value < 10 or value > 99:
            values_new.remove(value)
    return values_new

values_str : str = input()

values_split : list[str] = values_str.split(":")

values_int : list[int] = [int(values_split[i]) for i in range(len(values_split))]

list_remove_min_max = remove_min_max(values_int)

print(":".join(
    [str(list_remove_min_max[i]) for i in range(len(list_remove_min_max))]
    ))

list_remove_even = remove_even(values_int)

print(":".join(
    [str(list_remove_even[i]) for i in range(len(list_remove_even))]
    ))

list_remove_not_2_digit = remove_not_2_digit(values_int)

print(":".join(
    [str(list_remove_not_2_digit[i]) for i in range(len(list_remove_not_2_digit))]
    ))
