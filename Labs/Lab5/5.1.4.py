max_tickets: int = 100
tickets_sold: int = 0
buyers: int = 0 

while tickets_sold < max_tickets:
    tickets =   int(input(f"There are {max_tickets-tickets_sold} trickets left, you can at max 4 \n"
                            "Enter how many you want : "))
    if(tickets <= 4 and tickets <= max_tickets-tickets_sold and tickets > 0):
        tickets_sold += tickets
        buyers += 1
        print("Transaction concluded\n")
    else:
        print(f"{tickets} is not a valid number of tickets\n")

print(f"Total number of buyers : {buyers}")