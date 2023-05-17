#Write a Python program to convert all the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence.
def change_cases(s):
    return str(s).upper(), str(s).lower()
 
chrars = {'e', 'j', 'F', 'l', 'q', 'p', 'h', 'r', 'G'}
print("Original Characters:\n",chrars)
 
result = map(change_cases, chrars)
print("\nAfter converting above characters in upper and lower cases\nand eliminating duplicate letters:")
print(set(result))
