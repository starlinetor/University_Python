import matplotlib.pyplot as plt
import random

def smooth_graph(numbers : list[int], iteration : int) -> list[int]:
    """
    Smoothes a list of numbers and graphes it 
    """
    average : int = 0

    for i in range(len(numbers)): 
        #edge cases on the borders
        if i == 0: 
            average = (numbers[0] + numbers[1]) / 2
            continue
        if i == len(numbers) -1:
            average = (numbers[len(numbers)-1] + numbers[len(numbers)-2]) / 2
            numbers[i] = average
            continue
        #default cases
        average_temp = (numbers[i-1] +  numbers[i] + numbers[i+1] ) / 3
        numbers[i-1] = average
        average = average_temp
    plt.plot(range(len(numbers)), numbers, label = f"Smothed n : {iteration}")
    return numbers

#creates the list to be averaged
default_list : list[int] = []

for i in range(100):
    default_list.append(random.randint(1,100))

#plots default list
plt.plot(range(len(default_list)),default_list, label = "Default list")   

smooth_list : list[int] = default_list.copy()
#smothing
for i in range(100):
    smooth_list = smooth_graph(smooth_list, i)

plt.xlabel("Index")
plt.ylabel("Value")

#plt.legend()
plt.show()

