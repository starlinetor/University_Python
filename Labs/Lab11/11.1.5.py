def sparse_array_sum(a : dict[int:int], b : dict[int:int]):
    max_dimension = max(max(vector_1.keys()), max(vector_2.keys()))
    sparse_array = {}
    for i in range(1,max_dimension+1):
        component = a.get(i,0) + b.get(i,0)
        if component != 0:
            sparse_array[i] = component
    return sparse_array

vector_1 = {5:4, 9:2, 10:9} 
vector_2 = {2:12, 9:7, 15:21} 

print(sparse_array_sum(vector_1, vector_2))