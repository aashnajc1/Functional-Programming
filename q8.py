# Write a Python program to add two given lists and find the difference between lists.
def addition_subtrction(x, y):
    return x + y, x - y
 
nums1 = [5, 2, 1, 8]
nums2 = [1, 7, 5, 9]
print("Original lists:")
print(nums1)
print(nums2)
result = map(addition_subtrction, nums1, nums2)
print("\nResult:")
print(list(result))
