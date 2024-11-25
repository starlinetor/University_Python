customers : dict[str:int] = {}

def best_customer(customers : dict[str:int]) -> str:
    max_buy = max(customers.values())
    for customer in customers.keys():
        if customers[customer] == max_buy:
            return customer
    
while True:
    name = input("Name : ")
    buy = int(input("Buy : "))
    if name == "0":
        break
    customers[name] = buy
    
print(customers)

print(best_customer(customers))