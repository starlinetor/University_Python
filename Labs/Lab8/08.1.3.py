import random
from tracemalloc import start

def longest_range(range_1 : list[int], range_2 : list[int]) -> list[int]:
    """
    Given two tuples of lenght 2 that rappresent two ranges it will return the longest\n
    If the lenght is the same it will return the first
    """
    if(abs(range_1[1]-range_1[0]) >= abs(range_2[1]-range_2[0])):
        return range_1.copy()
    else : 
        return range_2.copy()


n_throws : int = 20

dice_throws : list[int] = [None] * n_throws
for i in range(n_throws):
    dice_throws[i] = random.randint(1,6)

b_start_stop = [0,0]
start_stop = [0,0]
number = dice_throws[0]

for i in range(n_throws):
    if dice_throws[i] != number:
        #we save where the sequence stops
        start_stop[1] = i-1
        #find if the last sequence was the longest
        b_start_stop = longest_range(b_start_stop, start_stop)
        #save new digit
        number = dice_throws[i]
        #save starting position
        start_stop[0] = i

for i in range(n_throws):
    if(i == b_start_stop[0]):
        print(f"({dice_throws[i]} ",end="")
    elif(i == b_start_stop[1]):
        print(f"{dice_throws[i]}) ",end="")
    else:
        print(f"{dice_throws[i]} ",end="")  
        