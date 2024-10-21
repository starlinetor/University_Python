n: int = int(input("Enter a number "))

for i in range(2,n+1):
    prime: bool = True

    for j in range(2, int(i/2+1)):
        if(i%j == 0):
            prime = False

    if (prime == True) :
        print(i) 
