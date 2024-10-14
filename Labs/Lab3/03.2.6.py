from os import TMP_MAX


income: int = int(input("Income : "))
married_str: str = input("Married ? y/n : ") 
married: bool

if(married_str in {"y", "Y", "yes", "Yes"}):
    married = True 
elif(married_str in{"n", "N", "no", "No"}):
    married = False
else:
    raise ValueError(f"{married_str} is not a recognized instruction")

tax: float = 0

if(not married):
    if(income <= 8000):
        tax = income*0.1
    elif(income <= 32000): 
        tax = 800 + (income - 8000) * 0.15 
    else:
        tax = 4400 + (income- 32000) * 0.25
else:
    if(income <= 16000):
        tax = income*0.1
    elif(income <= 64000): 
        tax = 1600 + (income - 16000) * 0.15 
    else:
        tax = 8800 + (income- 64000) * 0.25

print(tax)