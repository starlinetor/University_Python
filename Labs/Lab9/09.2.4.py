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

n = 10

table = [[i*10+j for j in range(n)] for i in range(n)]

print_table(table)

# TODO : needs to be finished