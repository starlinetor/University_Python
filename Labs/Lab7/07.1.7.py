import random

random_list : list[int] = []

for i in range(3):
    random_list.append(random.randint(0,99))
    
def sum_without_lowest(numbers: list[int]):
    numbers.remove(min(numbers))
    sum_n : int = 0
    for n in numbers:
        sum_n += n
    return sum_n

print(random_list)
print(sum_without_lowest(random_list))