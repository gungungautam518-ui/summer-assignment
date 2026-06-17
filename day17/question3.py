def find_intersection(nums1, nums2):
    
    return list(set(nums1) & set(nums2))

array1 = [4, 9, 5, 4]
array2 = [9, 4, 9, 8, 4]
print("Intersection:", find_intersection(array1, array2))

