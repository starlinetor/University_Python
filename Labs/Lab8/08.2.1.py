import random


def print_table(table : list[list[int]]) -> None:
    print("[ x ],",end="")
    for i in range(len(table[0])):
        print(f"[ {i} ],",end="")
    print()
    for i in range(len(table)):
        for j in range(len(table[i])):
            if(j != 0):
                print(", {:.2f}".format(table[i][j]),end="")
            else:
                print(f"[ {i} ],",end="")
                print("[",end="")
                print("{:.2f}".format(table[i][j]),end="")
        print("]")

def neighbor_average(values : list[list[float]], x:int, y:int):
    total_x : int = len(values[0])
    total_y : int = len(values)
    
    #row -> y
    #collumn -> x
    
    max_x = x + 1 if x + 1 < total_x else x
    min_x = x - 1 if x - 1 >= 0 else x
    max_y = y + 1 if y + 1 < total_y else y
    min_y = y - 1 if y -1 < total_y else y
    
    print(f"range : ({min_x},{min_y})({max_x},{max_y})")
    total : float = 0
    n : int = 0
    for i in range(min_x,max_x+1,1):
        for j in range(min_y,max_y+1,1):
            print(f"({i},{j}) : {values[j][i]}")
            total += values[j][i] 
            n += 1
    avrage : float = total / n
    print (f"avrage : {avrage}")

#colums
n = random.randint(5,10) 
#rows
m = random.randint(5,10)
#init a table with random values
table = [[round(random.random(),2) for _ in range(n)] for _ in range(m)] 
print_table(table)

x = random.randint(0,m-1)
y = random.randint(0,n-1)

print(f"coordinates : ({x},{y})")

neighbor_average(table,y,x)