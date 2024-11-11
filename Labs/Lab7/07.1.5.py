def same_set(list_a : list, list_b : list ) -> bool:
    
    same : bool = True
    
    for element in list_a:
        if element not in list_b :
            same = False

    return same

print(same_set([1, 4, 9, 16, 9, 7, 4, 9, 11], [11, 11, 7, 9, 16, 4, 1]))
