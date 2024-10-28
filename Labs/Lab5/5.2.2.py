import random


x = 0 
y = 0

for i in range(100):
    crossing:int = random.randint(1,4)
    match crossing:
        case 1 :
            x += 1
        case 2 :
            x -= 1
        case 3: 
            y += 1
        case 4:
            y -= 1
    print(f"X : {x}, Y : {y}")