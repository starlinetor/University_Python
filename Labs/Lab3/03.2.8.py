money_spent : float = float(input("Money spent : "))

bonus : float = 0 

if(10 <= money_spent <= 60):
    bonus = 0.08
elif(money_spent <= 150):
    bonus = 0.1
elif(money_spent <= 210):
    bonus = 0.12
else:
    bonus = 0.14

print(f"Bonus : {int(bonus*100)}%") 