n: int = int(input("Enter nuber : ")) 

for i in range(n):
    print('*'*n)

print()

for i in range(n-1):
    print(' '*(n-i) + "*"*i*2+ "*" )

for i in range(n-1,-1,-1):
    print(' '*(n-i) + "*"*i*2+ "*" )