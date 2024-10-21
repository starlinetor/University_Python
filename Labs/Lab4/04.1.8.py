sequence: bool = False
sequence_number: int = 0
sequence_number_init: bool = False
valid_numbers: list[int] = []

while True:

    value_str:str = input("Enter a new number: ")

    if(value_str == ""):
        break

    value: int = int(value_str)

    if(sequence_number_init == False):
        sequence_number_init = True
        sequence_number = -value

    if (value == sequence_number and value not in valid_numbers):
        valid_numbers.append(value) 
    else:
        sequence_number = value

print(valid_numbers)

