
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

def check_square(magic_square : list[list[int]]) -> bool:
    tests : list[int] = []
    #diagonals
    tests.append(magic_square[0][0] + magic_square[1][1] + magic_square[2][2] + magic_square[3][3])
    tests.append(magic_square[0][0] + magic_square[1][1] + magic_square[2][2] + magic_square[3][3])
    #rows
    for i in range(4):
        tests.append(magic_square[i][0] + magic_square[i][1] + magic_square[i][2] + magic_square[i][3])
    #collums
    for i in range(4):
        tests.append(magic_square[0][i] + magic_square[1][i] + magic_square[2][i] + magic_square[3][i])
    #check all test are the same
    for test in tests : 
        if tests[0] != test : 
            return False
        
    return True

magic_square : list[list[int]] = [[0 for _ in range(4)] for _ in range(4)]

print_table(magic_square)

for i in range(4):
    for j in range(4):
        value : int = -1
        valid_range = [i+1 for i in range(16)]
        while True: 
            value = int(input("Enter a number between 1 and 16 : "))
            if(value in valid_range):
                break
            print("Value not valid")
        magic_square[i][j] = value
        print_table(magic_square)

print(check_square(magic_square))

