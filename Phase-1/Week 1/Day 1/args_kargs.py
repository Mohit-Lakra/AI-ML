# args* and kwargs** in Python

def example_function(*args, **kwargs):
    print("Positional arguments (args):")
    for arg in args:
        print(arg)
    
    print("\nKeyword arguments (kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
example_function(1, 2, 3, name="Alice", age=30, city="New York")

# args allows you to pass a variable number of positional arguments to a function.
# kwargs allows you to pass a variable number of keyword arguments to a function.
