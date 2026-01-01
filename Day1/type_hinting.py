# type hinting in python
# Type hinting is a feature in Python that allows you to specify the expected data types of variables, function parameters, and return values. This can help improve code readability and make it easier to catch type-related errors during development.

def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}!"

# advanced type hinting with lists and dictionaries
from typing import List, Dict

def process_numbers(numbers: List[int]) -> List[int]:
    return [n * 2 for n in numbers]

def process_user_info(user_info: Dict[str, str]) -> str:
    return f"User {user_info['name']} is from {user_info['city']}."


