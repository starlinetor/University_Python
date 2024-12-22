from io import TextIOWrapper
from os import sep

#this tuple stores all separators, add if needed
separators = (" ", ",")

#get input file for bad words
inf_bad_words : TextIOWrapper = open("11.1.4_bad_words.txt", "r", encoding="utf-8") 

inf_bad_words_list : list[str] = inf_bad_words.readlines()

inf_bad_words.close()

bad_words_list : list[str] = []
#extract the bad words
for line in inf_bad_words_list : 
    split_line = line.removesuffix("\n").split(",")
    for word in split_line:
        bad_words_list.append(word.strip().strip("'"))
#save the bad words in a set
bad_words : set = set(bad_words_list)
#open raw text
inf_raw_text = TextIOWrapper = open("11.1.4_raw_text.txt", "r", encoding="utf-8")

raw_text = inf_raw_text.readlines()

inf_raw_text.close()

raw_text_list : list[str] = []

word_list : list[str] = []
#get all words
for line in raw_text:
    for char in line:
        #checks if a char is a "letter" or a separator
        if char.lower() not in separators:
            word_list.append(char)
        else:
            #if not it saves the list and the separator
            if len(word_list) > 0:
                word_str : str = "".join(word_list)
                raw_text_list.append(word_str)
                word_list = []
            raw_text_list.append(char)

censored_text_list : list[str] = []
#censor words
for word in raw_text_list:
    if word in bad_words:
        word = "*"*len(word)
    censored_text_list.append(word)

outfile : TextIOWrapper = open("11.1.4_censored_text.txt", "w", encoding="utf-8") 

outfile.write("".join(censored_text_list))