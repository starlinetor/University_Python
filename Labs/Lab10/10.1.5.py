numbers : list[float] = []
second_try : bool = False

while True:
    number = input("Enter number : ")
    
    if number == " ":
        break
    
    try : 
        numbers.append(float(number))
        second_try = False
    except:
        print("Invalid number")
        second_try = True
        continue
    
    if second_try == True : 
        exit()

print(sum(numbers))