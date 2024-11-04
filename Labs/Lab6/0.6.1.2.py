def count_words (string : str) -> int:
    """
    Returns the number of words in a given string\n
    A word is a sequence of character separated by 1 or more spaces
    
    :Param:\n 
    string - simple word \n
    :Return:\n
    int - number of words\n
    """
    
    word : bool = False
    words : int = 0
    
    for char in string:
        if not word and char != " ":
            word = True
            words +=1
        if word and char == " ":
            word = False
    
    return words