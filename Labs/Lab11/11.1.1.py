from io import TextIOWrapper

from numpy import sort

#alphabeth
alphabeth : tuple[str] = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
#read file
infile : TextIOWrapper = open("11.1.1_input.txt", "r", encoding="utf-8")
#file to list of strings
infile_list = infile.readlines()
# create a vocabulary for each word
words : dict[str:int] = {}
#empty word
word_list : list[str] = []

for line in infile_list:
    for char in line:
        if char.lower() in alphabeth:
            word_list.append(char.lower())
        elif len(word_list) > 0 : 
            word_str : str = "".join(word_list)
            if word_str in words.keys():
                words[word_str] += 1
            else : 
                words[word_str] = 1
            word_list = []

for key in words.keys():
    print(f"{key} : {words[key]}")