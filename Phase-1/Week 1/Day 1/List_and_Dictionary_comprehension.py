# Old way
squares = []
for i in range(1, 11):
    squares.append(i * i)
print(squares)

# New way - List Comprehension
# Syntax: [expression for item in iterable if condition]

squares_comp = [i * i for i in range(1, 11)]
print(squares_comp)


# Dictionary Comprehension

label = ["apple", "banana", "cherry"]
price = [0.5, 0.3, 0.2]

label_price_dict = {label[i]: price[i] for i in range(len(label))}
print(label_price_dict)
