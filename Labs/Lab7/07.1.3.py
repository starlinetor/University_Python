from tkinter import N


def remove_min(numbers : list[int]) -> list[int] : 
    """
    Removes the minimum of the list without using min or remove
    """ 
    lowest_number = numbers[0]
    #finds the lowest number
    for number in numbers :
        if number < lowest_number : 
            lowest_number = number
            
    lowest_removed : list[int] = []
    #creates new list without the lowest number
    for number in numbers: 
        if number != lowest_number:
            lowest_removed.append(number)
            
    return lowest_removed
            
print(remove_min([1,2,3,4,5,6,1,2,23,5,7,1,1231]))