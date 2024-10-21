string: str = input("Enter a string : ")

vocals = ('A','a','E','e','I','i','O','o','U','u')

upper_letters: list[str] = []
even_letters: list[str] = []
underscore_vocals: list[str] = []
n_numbers: int = 0
position_vocals: list[int] = []

for char in string:
    #the letter is lower case
    if(char.isupper()):
        upper_letters.append(char)
    #the letter index is even
    if(string.index(char)%2==0 and char.isalpha()):
        even_letters.append(char)
    #change letters with '_'
    #save the position of vocals
    if(char in vocals):
        underscore_vocals.append('_')
        position_vocals.append(string.index(char))
    else:
        underscore_vocals.append(char)
    #number of numbers in the string
    if(char.isnumeric()):
        n_numbers += 1

print(
    f"Upper letters only string : {"".join(upper_letters)}\n"
    f"Even letters only string : {"".join(even_letters)}\n"
    f"Vocals replaced with '_' {"".join(underscore_vocals)}\n"
    f"Vocals index : {position_vocals}\n"
    f"Number of numeric values present : {n_numbers}"
)