def remove_non_letters(set_char : set[str]) -> set[str]:
    global alphabeth
    set_char_copy = set_char.copy()
    for char in set_char_copy:
        if char not in alphabeth:
            set_char.remove(char)
    return set_char

alphabeth : list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

string_1 : str = "gino hated milk with balls"
string_2 : str = "armadillo is an odd word"

set_1 : set[str] = set(string_1)
set_2 : set[str] = set(string_2)

set_1 = remove_non_letters(set_1)
set_2 = remove_non_letters(set_2)

intersection : list[str] = []
subtraction_1 : list[str] = []

for char in set_1:
    if char in set_2:
        intersection.append(char)
    if char not in set_2:
        subtraction_1.append(char)

subtraction_2 : list[str] = []
for char in set_2:
    if char not in set_1:
        subtraction_2.append(char)

missing_letters : list[str] = []

for char in alphabeth:
    if char not in set_1 and char not in set_2:
        missing_letters.append(char)

print(f"intersection : {intersection}")
print(f"subtraction_1 : {subtraction_1}")
print(f"subtraction_2 : {subtraction_2}")
print(f"missing letters : {missing_letters}")