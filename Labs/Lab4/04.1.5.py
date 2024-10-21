n: int = int(input("Enter a number "))

prime: bool = True

for i in range(2, int(n/2+1)):
    if(n%i == 0):
        prime = False

print(f"{n} is prime : {prime}")