def shift_list(values : list) -> list: 
    """
    Shifts all elements in a list one to the right\n
    Loops over the last element
    """
    #find the lenght of the list
    lenght_list : int = len(values)
    
    #create a new emtpy list
    shifted_values : list = [None] * lenght_list

    #move all the elements one to the right
    for i in range(1,lenght_list,1):
        shifted_values[i] = values[i-1]
    
    #save last element to the first index
    shifted_values[0] = values[lenght_list-1]
    
    return shifted_values
    
numbers : list[int] = [1,2,3,4,5,6,7,8]

print(shift_list(numbers))