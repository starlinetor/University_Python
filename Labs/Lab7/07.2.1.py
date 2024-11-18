import random

random_list : list[int] = []

for i in range(5):
    random_list.append(random.randint(0,99))

starting_list = random_list

average : int = 0

for i in range(len(random_list)): 
    #edge cases on the borders
    if i == 0: 
        average = (random_list[0] + random_list[1]) / 2
        continue
    if i == len(random_list) -1:
        average = (random_list[len(random_list)-1] + random_list[len(random_list)-2]) / 2
        random_list[i] = average
        continue
    #default cases
    average_temp = (random_list[i-1] +  random_list[i] + random_list[i+1] ) / 2
    random_list[i-1] = average
    average = average_temp

print(starting_list)    
print(random_list)

