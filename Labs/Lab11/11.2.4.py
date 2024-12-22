from copy import copy, deepcopy
from math import cos, pi, sin

def corridor_exists(x : int, y : int, maze) -> bool:
    if y < len(maze) and x < len(maze[y]) and maze[y][x] == " ":
        return True
    return False

def print_maze(maze : list[str], paths : dict[tuple[int]:str]):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if (x,y) in paths.keys():
                print(paths[(x,y)], end="")
            else:
                print("*", end="")
        print()
    print()

infile = open("11.2.4_maze.txt", "r", encoding="utf-8")

infile_list = infile.readlines()

infile.close()

#clean junk and make a better format
for i in range(len(infile_list)):
    infile_list[i] = infile_list[i].removesuffix("\n")

corridors : dict[tuple[int] : list[tuple[int]]] = {}

#create all corridors
for y in range(len(infile_list)):
    for x in range(len(infile_list[y])):
        if infile_list[y][x] == " ":
            corridors[(x,y)] = []
            for i in range(4):
                if corridor_exists(x + int(sin(pi/2*i)), y + int(cos(pi/2*i)), infile_list):
                    corridors[(x,y)].append((x + int(sin(pi/2*i)), y + int(cos(pi/2*i))))

paths : dict[tuple[int]:str] = {}

for key in corridors.keys():
    paths[key] = "?"

for y in range(len(infile_list)):
    for x in range(len(infile_list[y])):
        #if we are not in the border we continue
        if x != 0 and x != len(infile_list[y])-1 and y != 0 and y != len(infile_list)-1  or (x,y) not in paths.keys():
            continue
        #each case on the border
        if x == 0:
            paths[(x,y)] = "W"
        elif x == len(infile_list[y])-1:
            paths[(x,y)] = "E"
        elif y == 0:
            paths[(x,y)] = "N"
        elif y == len(infile_list)-1:
            paths[(x,y)] = "S"
        else : 
            print(f"Error : x : {x}, y : {y}")

print_maze(infile_list, paths)

while True:
    changes = False
    
    paths_temp = deepcopy(paths)
    
    for path in paths.keys():
        #create a temporary paths variable
        
        if paths[path] != "?":
            continue
        for possible_path in corridors[path]:
            if paths[possible_path] == "?":
                continue
            #we found a path, we changed the maze so we keep iterating
            changes = True
            x = possible_path[0] - path[0]
            y = possible_path[1] - path[1]
            if x == 1:
                paths_temp[path] = "E"
            elif x == -1:
                paths_temp[path] = "W"
            elif y == 1:
                paths_temp[path] = "S"
            elif y == -1:
                paths_temp[path] = "N"
    
    paths = deepcopy(paths_temp)
    
    if changes == False:
        break
    input()
    print_maze(infile_list, paths)
