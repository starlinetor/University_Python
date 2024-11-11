from operator import index
import random
from threading import local

random_list : list[int] = []

for i in range(10):
    random_list.append(random.randint(1,100))

local_maximums : list [int] = []    

for i in range(len(random_list)):
    #edge cases on the borders
    if i == 0 and random_list[0] > random_list[1]: 
        local_maximums.append(0)
        continue
    if i == len(random_list) -1 and random_list[i] > random_list[i-1]:
        local_maximums.append(i)
        continue
    #default cases
    if random_list[i] > random_list[i-1] and random_list[i] > random_list[i+1]:
        local_maximums.append(i)

#no two maximums can be more distant than the lenght of the list itself
distance = len(random_list)
closest_maximums : tuple[int] = (0,0)

for i in range(len(local_maximums)-1):
    if local_maximums[i+1]-local_maximums[i] < distance:
        distance = local_maximums[i+1]-local_maximums[i]
        closest_maximums = (local_maximums[i],local_maximums[i+1])

print(f"List : {random_list}")

if len(local_maximums) == 0 : 
    print("No local maximum")
else : 
    print(f"Index of maximums {local_maximums}")
    print(f"Closests maximums positions {closest_maximums}")