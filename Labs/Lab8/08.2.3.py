
def print_table(table : list[list[str]]) -> None:
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

def game_won(tris_board : list[list[str]]) -> Boolean:
    win_states : list[list[tuple[int]]] = [
        #diagonals
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)],
        #collums
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        #rows
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)]
    ]
    for win_state in win_states:
        (y1,x1) = win_state[0]
        (y2,x2) = win_state[1]
        (y3,x3) = win_state[2]
        #for each line it checks if all the simbols are the same and the line is made by empty spaces
        if(tris_board[y1][x1] == tris_board[y2][x2] and tris_board[y1][x1] == tris_board[y3][x3] and tris_board[y1][x1] != " " ):
            return True
    return False

def tris_input(tris : list[list[str]]) -> tuple[int]:
    #valid range
    valid_range = [0,1,2]
    while True:
        x : int = int(input("x : "))
        y : int = int(input("y : "))
        #verify valid input
        if x in valid_range and y in valid_range and tris[y][x] == " " :
            break
        print("Invalid coordinates")
    return(x,y)

def main() : 
    #variables
    x_player = True
    
    #tris play field
    tris : list[list[str]] = [[" " for _ in range(3)] for _ in range(3)]
    print_table(tris)

    for _ in range(9): 
        print("X player turn") if x_player else print("O player turn")
        print("Enter x and y coordinates")
        #input
        (x,y) = tris_input(tris)
        #add move to the board
        tris[y][x] = "X" if x_player else "O"
        print_table(tris)
        #if one player wins the game ends
        if(game_won(tris)):
            print("X player has won" if x_player else "O player has won")
            return
        #switch player
        x_player = not x_player
    #if neither player wins the game ends in a draw
    print("Game ended in a draw")

if __name__ == "__main__":
    main()
    
