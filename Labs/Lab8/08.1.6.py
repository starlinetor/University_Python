def merge_sorted(list_a : list[int],list_b : list[int]) -> list[int]:
    """
    Given two sorted slists it merges them keeping the merged list sorted
    """
    #initialization of the new list
    merged_list : list[int] = []
    #append the lowest number
    while(len(list_a)>0 and len(list_b)>0):
        if list_a[0]<list_b[0]:
            merged_list.append(list_a.pop(0))
        else:
            merged_list.append(list_b.pop(0))
    #find the list that is left
    list_left : list[int] = list_b if len(list_a) == 0 else list_a 
    while(len(list_left)>0):
        merged_list.append(list_left.pop(0))
    #return merged list
    return merged_list

a = [1,4,9,16]
b = [1,1,1,1,1,1]

print(merge_sorted(a,b))