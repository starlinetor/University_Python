from io import TextIOWrapper

from numpy import sort

def greater_than_list(number : int, number_list : list[int]) -> bool:
    for n in number_list:
        if number > n:
            return True
    return False


#alphabeth
alphabeth : tuple[str] = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
#read file
infile : TextIOWrapper = open("11.1.1_input.txt", "r", encoding="utf-8")
#file to list of strings
infile_list = infile.readlines()

infile.close()
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

most_common_words_value : list[int] = [0,0,0,0,0]
most_common_words : list[str] = ["","","","",""]


for key in words.keys():
    if greater_than_list(words[key], most_common_words_value):
        #append key and value
        most_common_words_value.append(words[key])
        most_common_words.append(key)
        #find lowest value
        lowest_value = min(most_common_words_value)
        lowest_value_index = most_common_words_value.index(lowest_value)
        #remove lowest value
        most_common_words.remove(most_common_words[lowest_value_index])
        most_common_words_value.remove(most_common_words_value[lowest_value_index])

#create a copy to be sorted
sorted_most_common_words_value : list[int] = reversed(sort(most_common_words_value))

for value in sorted_most_common_words_value:
    print(f"{most_common_words[most_common_words_value.index(value)]} : {value}")
    #remove the printed words, this is needed because if words have the same count they will be printed twice
    most_common_words_value[most_common_words_value.index(value)] = 0