pin: int = 1234
tries : int = 3

while (tries > 0): 
    digited_pin = int(input("Enter PIN : "))
    if(pin == digited_pin):
        break
    else : 
        print("Your PIN is incorrect")
        
    tries -= 1
    
if(tries == 0 ): 
    print("Your bank card is blocked")
else:
    print("Your PIN is correct")