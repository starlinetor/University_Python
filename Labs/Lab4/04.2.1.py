import math
import random

def biggest_pow_2 (number: int) -> int:
    '''
    returns biggest power of two that is less than number 
    '''

    return int(math.pow(2,int(math.log2(number))))

def computer_play(stupid: bool, marbles: int) -> int:
    '''
    Given a strategy and the number of marbles the computer returns a the number of marbles to be removed
    '''

    random_value: int = random.randint(1, int(marbles/2))

    if(stupid):
        print(f"The computer removed {random_value}")
        return random_value
    
    if(marbles == biggest_pow_2(marbles+1)-1):
        print(f"The computer removed {random_value}")
        return random_value

    return marbles - biggest_pow_2(marbles) + 1

def human_play(marbles: int) -> int:
    value: int = int(input("Enter marbles to be remeoved  : "))
    while value not in range(1, int(marbles/2)+1):
        print(f"Marbles to be removed must be between 1 and {int(marbles/2)}")
        value: int = int(input("Enter marbles to be remeoved  : "))
    return value

def write_state(computer_stupid: bool, computer_playing: bool, marbles: int):
    print(f"There are {marbles} marbles left")
    if (computer_playing):
        print(f"{"Stupid " if computer_stupid else "Smart "}computer next to play")
    else : 
        print("Human next to play")


marbles: int = random.randint(10,100)

computer_playing: bool = random.choice((True, False))
computer_stupid: bool = random.choice((True, False))

while marbles != 1: 

    write_state(computer_stupid,computer_playing,marbles)

    if computer_playing:
        marbles -= computer_play(computer_stupid,marbles)
    else:
        marbles -= human_play(marbles)
    
    computer_playing =  not computer_playing

write_state(computer_stupid,computer_playing,marbles)

print(f"The {"Computer" if computer_playing else "Human"} lost the game because had to take the last marble")