from math import cos, pi, sin

def corridor_exists(x : int, y : int, maze) -> bool:
    if y < len(maze) and x < len(maze[y]) and maze[y][x] == " ":
        return True
    return False

infile = open("11.2.3_maze.txt", "r", encoding="utf-8")

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

print(corridors)