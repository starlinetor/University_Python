import random

def print_table_int(table : list[list[int]]) -> None:
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

def print_table_str(table : list[list[str]]) -> None:
    print("[x]",end="")
    for i in range(len(table[0])):
        print(f"[{i}]",end="")
    print()
    for i in range(len(table)):
        for j in range(len(table[i])):
            if(j != 0):
                print(f", {table[i][j]}",end="")
            else:
                print(f"[{i}]",end="")
                print("[",end="")
                print(f"{table[i][j]}",end="")
        print("]")

table : list[list[int]] = [[random.randint(1,10) for _ in range(10)] for _ in range(10)]

print_table_int(table)

for water_level in range(11):
    flodding : list[list[str]] = [["*" if table[j][i] <= water_level else " " for i in range(10)] for j in range(10)]
    print_table_str(flodding)
    input()