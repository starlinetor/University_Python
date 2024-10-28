def lowest_divisor(n: int) -> int:
    """
    Finds the lower prime divisor given a number n \n
    Returns the lowest divisor i 
    """
    #we don't have to check if i is prime because if it wasn't we would have already fond a divisor earlier
    for i in range(2,int(n/2+1)): 
        if  n%i == 0:
            return i
    return n


divisors: list[int] = []
done: bool = False

n: int = int(input("Enter a number : "))            

while  done == False:
    print("Divisor Found")
    divisor = lowest_divisor(n)
    divisors.append(divisor)
    if(n == divisor):
        done = True
    n = n // divisor
    
print(", ".join(map(str, divisors)))