number: int = 10232

if(len(str(number)) != 5):
    print("number has to have 5 digits")
    quit()

for i in range(5):
    print(str(number)[i:i+1:])