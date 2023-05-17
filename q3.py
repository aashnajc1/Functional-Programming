# Write a Python program to sort a given list of strings(numbers) numerically
# using lambda.

def sort_numeric_strings(nums_str):
    result = sorted(nums_str, key=lambda el: int(el))
    return result
nums_str = ['5','11','47','6','0','101','203','-15','-511']
print("Original list:")
print(nums_str)
print("\nSort the said list of strings(numbers) numerically:")
print(sort_numeric_strings(nums_str))
