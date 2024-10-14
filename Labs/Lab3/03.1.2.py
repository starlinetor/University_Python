text: str = input("Input string : ")

if(text.isalpha()):
    print("The string is alphabetic only")
if(text.isupper()):
    print("The string is upper case only")
if(text.islower()):
    print("The string is lower case only")
if(text.isdecimal()):
    print("The string is decimal only")
if(text.isalnum()):
    print("The string is alphanumeric")    
if(text[0].isupper()):
    print("The string starts with an upper case letter")
if(text[len(text)-1] == '.'):
    print("The string ends with a dot")
