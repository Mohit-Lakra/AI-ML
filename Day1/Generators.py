# Generators in Python
# Generators are a simple and powerful tool for creating iterators. They allow you to declare a function that behaves like an iterator, i.e., it can be used in a for loop.
# Memory and Time Efficiency Comparison

import time

def square(n):
    res = []
    for i in range(1,n+1):
        res.append(i * i)
    return res

def square_generator(n):
    for i in range(1,n+1):
        yield i * i


start_time = time.time()
nums = square(100000000)
end_time = time.time()
print(f"Time taken by square function: {end_time - start_time} seconds")
start_time = time.time()
gen_nums = square_generator(100000000)
end_time = time.time()
print(f"Time taken by square_generator function: {end_time - start_time} seconds")
