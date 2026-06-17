def find_union(arr1, arr2):

    union_set = set(arr1) | set(arr2)
    
   
    return list(union_set)


array_a = [1, 2, 3, 2, 1]
array_b = [3, 2, 4, 5, 4]
print("Union:", find_union(array_a, array_b))

