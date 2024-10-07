def interest(balance,percentage):
    return balance + balance * percentage

balance = 1000.0

interestPercentage = 0.05

for i in range(1,4):
    balance = interest(balance, interestPercentage)
    print("In year",i,"your balance is",balance)