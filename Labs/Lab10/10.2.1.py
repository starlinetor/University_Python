alphabet : list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

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

#add the key to the cipher
for i in range(len(key_list)-1,-1,-1):
    cipher.append(key_list[i])

#invert the cipher
cipher = cipher[::-1]
#input
while True:
    encode_decode = input("Enter e to encode, d to decode : ").lower()
    if encode_decode == "e" or encode_decode == "d":
        break
    else :
        print(f"{encode_decode} is not a valid option")

encode = True if encode_decode == "e" else False

message = input("Enter the message, everything but letters will be ignored : ").lower()

#decode encode
new_message : list[str] = []
for letter in message:
    if letter not in alphabet : 
        new_message.append(letter)
    elif encode:
        new_message.append(cipher[alphabet.index(letter)])
    else : 
        new_message.append(alphabet[cipher.index(letter)])

#print new message
print("".join(new_message))