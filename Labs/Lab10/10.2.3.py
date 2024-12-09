from curses.ascii import isalpha
import math


def encode_decode(cipher : list[str],word : str):
    if len(word) == 1:
        return word
    if len(word) != 2: 
        raise ValueError("encode_decode must take two and only one or two letters as input")

    index_1 = cipher.index(word[0])
    index_2 = cipher.index(word[1])
    #get x and y cords
    x_1 = index_1 % 5
    y_1 = math.floor(index_1 / 5)

    x_2 = index_2 % 5
    y_2 = math.floor(index_2 / 5)
    
    new_index_1 = x_2 + y_1 * 5
    new_index_2 = x_1 + y_2 * 5 
    
    return(cipher[new_index_1] , cipher[new_index_2])

alphabet : list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

key_str = input("Key : ").lower()
key_list : list[str] = []

#change the string in to a list and remove duplicates
for letter in key_str:
    if letter not in alphabet:
        continue
    if letter not in key_list:
        key_list.append(letter)

#remove key letters in the cipher
cipher : list[str] = []
for letter in alphabet:
    if letter not in key_list:
        cipher.append(letter)

#invert cipher
cipher = cipher[::-1]

#add the key to the cipher
for i in range(len(key_list)-1,-1,-1):
    cipher.append(key_list[i])

#invert cipher again
cipher = cipher[::-1]

message = input("Enter the message, everything but letters will be ignored : ").lower()

#decode encode
new_message : list[str] = []
#save all letters and characters
for letter in message:
    new_message.append(letter)
#create a list of letters to change
letters : list[list[str|int]] = []
#save the position of each letter
for i in range(len(new_message)):
    if new_message[i].isalpha():
        letters.append([new_message[i], i])

#remove the last element if the letters are not even
if len(letters) % 2 != 0:
    letters.pop()

for i in range(0,len(letters),2):
    letter_1, letter_2 = encode_decode(cipher, letters[i][0] + letters[i+1][0])
    new_message[letters[i][1]] = letter_1
    new_message[letters[i+1][1]] = letter_2

#print new message
print("".join(new_message))