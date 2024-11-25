prices = [
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
    [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
    [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]
]

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

def get_ticket(tickets : list[list[int]], x : int , y : int) -> bool:
    """
    given x and y it will set the price to zero and return True\n
    if the price is already zero it will return false
    """
    if tickets [y][x] == 0:
        return False
    tickets[y][x] = 0
    return True

def from_price_ticket(tickets: list[list[int]], price) -> tuple[int] | bool:
    """
    returns an x and y of the first ticket with the selected price
    """
    for i in range(len(tickets)):
        for j in range(len(tickets[i])):
            if tickets[i][j] == price:
                return (j,i)
    return False

command : str  = " "

while command != "q":
    command = input("Enter q to exit, price or ticket : ")
    if command == "q":
        break
    if command == "ticket":
        print_table(prices)
        x : int = int(input("x : "))
        y : int = int(input("y : "))
        get_ticket(prices,x,y)
    if command == "price":
        while True:
            print_table(prices)
            price : int = int(input("Desired price : "))
            ticket = from_price_ticket(prices, price)
            if not ticket:
                print("Invalid price")
            else : 
                break
        x, y = ticket
        get_ticket(prices, x, y)
        
        