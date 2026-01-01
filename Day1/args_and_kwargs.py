# args and kwargs in Python

def multiply(*args):
    res = 1;
    for i in args:
        res *= i
    return res

def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(multiply(1, 2, 3, 4))  # Output: 24
greet(name="Alice", age=30, city="New York")
