# Write a Python program to calculate sum of numbers from the list and maximum element from the list
from functools import reduce
def sum(a,b):
    print(f"a={a}, b={b}, {a}+{b}={a+b}")
    return a+b
scores=[76,78,80,91,92]
total=reduce(sum,scores)
print(total)
