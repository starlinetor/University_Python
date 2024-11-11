sequence : list[int] = []
while True:
    value : str = input("Enter a number, q to exit : ")
    if (value == 'q'):
        break
    sequence.append(int(value))
    
add : bool = True
total : int = 0    
sign : str = ""    
    
for number in sequence:

    #this is at the start to prevent the first sign to be printed
    print(f" {sign} {number}",end="")

    #the signes are inverted : add -> -, subtract -> + because they are chosen after priting so they predict the next one
    if (add == True):
        add *= -1
        total += number
        sign = "-"
    else : 
        add *= -1
        total -= number
        sign = "+"
        

    
print(f" = {total}")

