def merge(list_a : list, list_b : list) -> list:
    if len(list_a) < len(list_b) : 
        short_lenght : int = len(list_a)
        long_list : list = list_b
    else : 
        short_lenght : int = len(list_b)
        long_list : list = list_a
        
    merged_list : list = []
    
    for i in range(short_lenght):
        merged_list.append(list_a[i])
        merged_list.append(list_b[i])
        
    for i in range(short_lenght, len(long_list),1):
        merged_list.append(long_list[i])
    return merged_list

a = ["a","b","c","d"]
b = [1,2,3,4,5,6,7,8,9]

print(merge(a,b))
print(merge(b,a))