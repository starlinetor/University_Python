import random

random_list : list[int] = []

for i in range(20):
    random_list.append(random.randint(0,99))
    
print(random_list)
random_list.sort()
print(random_list)