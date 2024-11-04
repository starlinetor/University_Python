roman_numerals : dict[str:int] = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

#these have been hardocded because these are the only possible subtractions
#any other is wrong, for exemple VX is not valid
roman_subtraction : dict[str:int] = {
    "IV" : 4,
    "IX" : 9,
    "XL" : 40,
    "XC" : 90,
    "CD" : 400, 
    "CM" : 900
}

def is_roman(number : str) -> bool:
    """
    Returns True if the string is a roman number\n
    A roman number is a word made only by the following letters: \n
    I, V, X, L, C, D, M\n
    Lower case letters are counted
    """
    for char in number: 
        if char.upper() not in roman_numerals.keys():
            return False
    return True

def valid_sequence_roman(number : str) -> bool:
    """
    Returns true if the number is a valid roman number sequence\n
    A valid roman number is a number where no higher values are preceded by two or more lower values\n
    A valid roman number has only the following subtraction cases : \n
    IV, IX, XL, XC, CD, CM
    """
    lowest_number: int = 1000
    skip : bool = False
    
    for i in range(len(number)):
        if skip : 
            skip = False
            continue
        if i!= len(number)-1: 
            #we don't care about the last number so it can be skipped
            n1 : int = roman_numerals[number[i].upper()]
            n2 : int = roman_numerals[number[i+1].upper()] 
            n1_n2 : str = number[i:i+2].upper()
        else : 
            n1 = roman_numerals[number[i].upper()]
            n2 = roman_numerals[number[i].upper()]
        #we can't have a new number bigger than an old one
        if n1 > lowest_number : 
            return False
        #if n1 is greater than n2 then we can set the lowest number to n1 
        if n1 >= n2:
            lowest_number = n1
            continue
        #if the subtraction sequence is not valid we exit immediatly
        if n1_n2 not in roman_subtraction.keys():
            return False
        #n2 can't be greater than the lowest number, exemple : VIX
        if n2 > lowest_number:
            return False
        #if everything is fine we set n2 as the new lowest number and skip it
        #if for exemple we have LIX the lowest number should not be I but X 
        lowest_number = n2
        skip = True
    return True

def valid_repetition_roman(number : str) -> bool: 
    """
    Returns true if the roman number has a valid repetition\n
    A valid repetition are those where no more than 3 charcter are repeated
    """
    seen_number : str = ""
    counter : int = 0
    for char in number: 
        if char == seen_number: 
            counter += 1
        else : 
            seen_number = char
            counter = 1
        if counter == 4:
            return False
    return True
    
def valid_roman(number : str) -> bool:
    """
    Returns true if the number is a valid roman number\n
    A valid roman number needs to pass the following tests:\n
    1) Be only written with roman numbers\n
    2) Be a correct sequence of roman numbers\n
    3) Contain only the correct subtraction cases\n
    4) No letter is repeated more than 3 times
    """
    #checks for only correct subtraction
    if not is_roman(number) : 
        print("Some characters in the number are not roman numerals")
        return False
    if not valid_sequence_roman(number) : 
        print("The roman sequence is not valid")
        return False
    if not valid_repetition_roman(number):
        print("There are more than 3 repetitions")
        return False
    return True

def convert_roman(number : str) -> int:
    total : int = 0
    skip : bool = False
    for i in range(len(number)):
        if skip : 
            skip = False
            continue
        if i != len(number)-1: 
            #we don't care about the last number so it can be skipped
            n1 : int = roman_numerals[number[i].upper()]
            n2 : int = roman_numerals[number[i+1].upper()] 
            n1_n2 : int =  roman_subtraction.get(number[i:i+2].upper())
        else: 
            total += roman_numerals[number[i].upper()]
            return total
        if(n1 >= n2):
            total += n1
            continue
        total += n1_n2
        #skip next iteration, is not needed
        skip = True
    return total


if __name__ == "__main__":
    roman_number: str = "DXXI"

    if(valid_roman(roman_number)):
        print(convert_roman(roman_number))