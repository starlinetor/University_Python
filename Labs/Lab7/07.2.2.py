import random
from tracemalloc import start


def print_parking(parkings : list[bool]) -> None:
    #True -> Free parking
    #False -> Occupied praking
    for parking in parkings:
        if parking :
            print("_",end="")
        else : 
            print("X",end="")
    print()

def best_parking_spot(parkings : list[bool],debug = False) -> int:
    #needed if the last parking is not used so it can end the last sequence
    parkings.append(False)
    #returns index for best spot
    #variables
    free_spot : bool = False
    longest_sequence : int = 0
    best_starting_index : int = 0
    sequence : int = 0
    starting_index : int = 0
    #finds the longest sequence
    for i in range(len(parkings)):
        if debug : 
            print(f"i : {i}, free_spot : {free_spot}, sequence : {sequence}, starting_index : {starting_index}, longest sequence : {longest_sequence}, best starting index : {best_starting_index}")
        if free_spot and parkings[i]: 
            #continue free parking sequence
            sequence +=1
        elif parkings[i]:
            #start new parking sequence
            sequence = 1
            free_spot = True
            starting_index = i
        elif sequence > longest_sequence :
            #end parking sequence 
            free_spot = False
            longest_sequence = sequence
            best_starting_index = starting_index
        else : 
            free_spot = False
    #return best parking : middle of the longest sequence of free parkings
    parkings.pop()
    return best_starting_index + int(longest_sequence/2)

parking : list[bool] = []

for i in range(random.randint(10,40)):
    parking.append(True)
    
for i in range(len(parking)):
    print_parking(parking)
    parked : int = best_parking_spot(parking)
    parking[parked] = False

print_parking(parking)