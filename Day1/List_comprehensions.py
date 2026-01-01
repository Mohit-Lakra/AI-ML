n = [1,2,3,4,5,6,7,8,9,10]

# Noramal way to create a list of squares
squares = []
for i in n:
    squares.append(i**2)
print("Squares using normal way:", squares)

# Using list comprehension to create a list of squares
# Syntax: [expression for item in iterable if condition]

squares_lc = [i**2 for i in n]
print("Squares using list comprehension:", squares_lc)

# Using map and lambda to create a list of squares
squares_map = list(map(lambda x: x**2, n))
print("Squares using map and lambda:", squares_map) # readability is less

# List comprehension with condition to get even squares
even_squares = [i**2 for i in n if i % 2 == 0]
print("Even squares using list comprehension:", even_squares)

# Using list comprehension to create a list of tuples (number, square)
num_square_tuples = [(i, i**2) for i in n]
print("List of tuples (number, square):", num_square_tuples)

# Using list comprehension to flatten a nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [item for sublist in nested_list for item in sublist]
print("Flattened list using list comprehension:", flattened_list)
