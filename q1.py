# Q) Write a Python program to create Fibonacci series upto n using Lambda. 

def fibonacci(count):
    listA = [0, 1]
    any(map(lambda _:listA.append(sum(listA[-2:])),
         range(2, count)))
    return listA[:count]

print(fibonacci(8))
