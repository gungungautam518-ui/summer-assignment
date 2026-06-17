def find_common_elements(list1, list2):
    common = set(list1).intersection(set(list2))
    return list(common)
list_a = [1, 2, 3, 4, 5, 5]
list_b = [4, 5, 6, 7, 8]
result = find_common_elements(list_a, list_b)
print("Common elements:", result)

