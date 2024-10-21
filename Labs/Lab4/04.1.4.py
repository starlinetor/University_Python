string : str = input("Enter a string ")

print("Reversed string : ", end='')
for char in reversed(string):
    print(char, end='')
print()

print("Reversed string only uppercase : ", end='')
for char in reversed(string):
    if(char.isupper()):
        print(char, end='')

