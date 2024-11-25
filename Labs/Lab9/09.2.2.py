words = []
last_sillable = None

def get_last_sillable(string : str) -> str:
    return string[len(string)-2:len(string)]

def get_first_sillable(string : str) -> str:
    return string[0:2]


while True:
    word = input("word : ")
    if(word == "*"):
        break
    if(word in words) : 
        break
    if(last_sillable != get_first_sillable(word) and last_sillable != None):
        break
    
    last_sillable = get_last_sillable(word)
    words.append(word)

print("you lost")