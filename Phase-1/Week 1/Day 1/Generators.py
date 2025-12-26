# Generators
# Allows us to load one batch of data at a time instead of loading the entire dataset into memory
# Useful for large datasets that don't fit into memory

import sys

# standard function

def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result

# generator function
def square_numbers_gen(nums):
    for i in nums:
        yield i * i

N = 1000000
n = range(1, N + 1)
my_nums = square_numbers(n)
my_nums_gen = square_numbers_gen(n)

# Check memory size
print("Memory size of standard function output:", sys.getsizeof(my_nums))        # Large memory
print("Memory size of generator function output:", sys.getsizeof(my_nums_gen))   # Small memory

small_gen = square_numbers_gen(range(1, 11))
for num in small_gen:
    print(num)


