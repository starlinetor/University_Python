string : str = input()

for i in range(len(string)):
    for j in range(len(string) - i):
        print(string[j:j+i+1])
