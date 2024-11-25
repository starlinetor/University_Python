import math


def print_table(table : list[list[int]]) -> None:
    print("[x ]",end="")
    for i in range(len(table[0])):
        print(f"[{i} ]",end="")
    print()
    for i in range(len(table)):
        for j in range(len(table[i])):
            if(j != 0):
                print(", {:0=2d}".format(table[i][j]),end="")
            else:
                print(f"[{i} ]",end="")
                print("[",end="")
                print("{:0=2d}".format(table[i][j]),end="")
        print("]")

n = 9

table = [[0 for _ in range(n)] for _ in range(n)]

print_table(table)

min_x = 0
max_x = n-1
min_y = 0
max_y = n-1

x = 0
y = 0

total = 0

angle = 0
"""
0 ->
1 v
2 <-
3 ^

"""
end = False

while True:
    
    print_table(table)
    
    total += 1
    table[y][x] = total
    
    if end : 
        break
    
    if(min_x == max_x and min_y == max_y):
        #when we can't move anymore we exit
        end = True
    
    #angle cases
    if angle % 4 == 0 and x == max_x: # >
        min_y += 1
        angle = (angle + 1) % 4
    elif angle %4 == 1 and y == max_y: # v
        max_x -= 1
        angle = (angle + 1) % 4
    elif angle %4 == 2 and x == min_x: # <
        max_y -= 1
        angle = (angle + 1) % 4
    elif angle%4 == 3 and y == min_y: # ^
        min_x += 1
        angle = (angle + 1) % 4

    x += int(math.cos(angle * math.pi / 2))
    y += int(math.sin(angle * math.pi / 2))
    print(x,y, angle)
    input()

